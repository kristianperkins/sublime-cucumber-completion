import sublime, sublime_plugin, re, os

step_def_urls = []
ruby_regexp = re.compile(r'[/"]\^?(.*?)\$?[/"] do(.*)')
groovy_regexp = re.compile(r"[/']\^?(.*?)\$?[/']\) \{ (.*) ->")
step_def_regexps = {'groovy': groovy_regexp, 'rb': ruby_regexp}

background_completion = ("Background template", """Feature: $1<enter feature title>
    In order $2...
    As a ...
    I want

    Background: $3<enter background title - applies to every Scenario>
        Given $4

    Scenario: $5<enter scenario title>
        When $6""")
scenario_completion = ("Scenario template", """Scenario: $1<enter scenario title>
    When $2""")

whens = ['Given', 'When', 'Then', 'And', 'But', '*']

class GherkinFeatureAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within feature files
        file_name = view.file_name()
        if (not file_name): file_name = ''
        if (view.score_selector(0, 'text.gherkin.feature') == 0) and (not file_name.endswith('.feature')):
            return []
        line = view.substr(sublime.Region(view.line(locations[0]).a, locations[0]))
        if (not line.strip()):
            pad_len = 8 - len(line)
            padding = "".join([" " for x in range(pad_len)]) if pad_len > 0 else ""
            completions = [background_completion, scenario_completion] if locations[0] < 20 else [scenario_completion]
            completions += [(when, padding + when + " ") for when in whens]
            return completions
        else:
            regex_and_params = self.find_step_defs(view.window().folders())
            regex_and_params = sorted(regex_and_params, key=lambda tup: tup[0])
            print regex_and_params
            step_completions = [self.create_completion_text(*completion) for completion in regex_and_params]
            completions = [(c, c) for c in step_completions] + [sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS]
            return completions

    def find_step_defs(self, base_folders):
        step_matches = []
        for step_file, step_file_name in self.find_step_files(base_folders):
            for key in step_def_regexps:
                if step_file_name.endswith(key):
                    step_def_regexp = step_def_regexps.get(key)
                    for line in step_file:
                        # print(line)
                        m = step_def_regexp.search(line)
                        if m:
                            step_matches.append(m.groups())
                            print "appending: ", m.groups()
        return step_matches

    def find_step_files(self, base_folders):
        for base in base_folders:
            for (path, dirs, files) in os.walk(base):
                step_files = [f for f in files if any(f.lower().endswith(file_suffix) for file_suffix in ['steps.groovy', 'steps.rb'])]
                # print step_files
                for file_name in step_files:
                    print "found: " + file_name
                    with open(os.path.join(path, file_name)) as f:
                        yield f, file_name

    def create_completion_text(self, completion, fields):
        params = [x for x in re.split(',', fields)]
        field_chunks = [re.split(' ', x)[-1] for x in params]
        # print "completions %s, fields %s
        try:
            return '%s'.join(self.unbraced_chunks(completion)) % tuple(field_chunks)
        except:
            print "failed completion: %s fields: %s" % (completion, fields)
            return completion

    def unbraced_chunks(self, txt):
        chunk = ''
        depth = 0
        for char in txt:
            if char == '(':
                if depth == 0:
                    yield chunk
                    chunk = ''
                depth = depth + 1
            elif char == ')' and depth > 0:
                depth = depth - 1
            elif depth == 0:
                chunk = chunk + char
        yield chunk
