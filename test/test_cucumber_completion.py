import os

import sublime, sublime_plugin
from CucumberFeatureAutocomplete import CucumberFeatureAutocomplete

completer = CucumberFeatureAutocomplete()

# def test_completer_with_empty_view():
#     completer.on_query_completions(Mock(), '', './examples')

# test examples found in the examples dir
def test_examples():
    tests = [d for d in os.listdir('examples') if not d.endswith('expected')]
    for d in tests:
        yield check_examples, d

def check_examples(d):
    message = "expectations failed for completions in {0}; found:\n{1}"
    test_dir = 'examples/{0}'.format(d,)
    expected = set(open('{0}.expected'.format(test_dir,)).read().splitlines())
    found = set(completer.find_completions([test_dir]))
    assert expected == found, message.format(d, found)
