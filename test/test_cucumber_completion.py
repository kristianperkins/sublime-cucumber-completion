from os import listdir, path


import sublime, sublime_plugin
from CucumberFeatureAutocomplete import CucumberFeatureAutocomplete

completer = CucumberFeatureAutocomplete()
ex = 'examples'
# test all example step definitions found in the examples directory
def test_examples():
    tests = [d for d in listdir(ex) if path.isdir(path.join(ex, d))]
    for d in tests:
        yield check_examples, d

def check_examples(d):
    message = "expectations failed for completions in {0}; found: '{1}'"
    test_dir = path.join(ex, d)
    expected = set(open('{0}.expected'.format(test_dir)).read().splitlines())
    found = set(completer.find_completions([test_dir]))
    assert expected == found, message.format(d, "', '".join(found))
