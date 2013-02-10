from os import listdir, path

import sublime
import sublime_plugin

from CucumberFeatureAutocomplete import CucumberFeatureAutocomplete

completer = CucumberFeatureAutocomplete()
ex = 'examples'


def test_examples():
    """test all example step definitions found in the examples directory"""
    tests = [d for d in listdir(ex) if path.isdir(path.join(ex, d))]
    for d in tests:
        yield check_examples, d


def check_examples(d):
    message = "expectations failed for completions in {0}; found: '{1}'"
    test_dir = path.join(ex, d)
    expected = set(open('{0}.expected'.format(test_dir)).read().splitlines())
    found = set(completer.find_completions([test_dir]))
    assert expected == found, message.format(d, "', '".join(found))


def test_splitting_regex_by_no_groups():
    assert list(completer.unbraced_chunks("no groups")) == ["no groups"]


def test_splitting_regex_by_groups():
    chunks = list(completer.unbraced_chunks('The customers name is (.*)'))
    assert ['The customers name is ', ''] == chunks
    chunks = list(completer.unbraced_chunks('Mrs (.*) is a customer'))
    assert ['Mrs ', ' is a customer'] == chunks
    chunks = list(completer.unbraced_chunks('(Mr|Mrs|Ms) (.*) is a customer'))
    assert ['', ' ', ' is a customer'] == chunks


def test_splitting_regex_ignores_inner_braces():
    chunks = list(completer.unbraced_chunks('More (braces (arent)) groups'))
    assert ['More ', ' groups'] == chunks
