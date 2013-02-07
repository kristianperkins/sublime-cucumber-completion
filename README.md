Cucumber Completion
===================

[![Build Status](https://travis-ci.org/krockode/cucumber-completion.png?branch=master)](https://travis-ci.org/krockode/cucumber-completion)

Sublime plugin to auto complete Cucumber step definitions.

Installation
------------

While inside the Sublime Packages directory (which is found inside [the data directory][1]),
clone the repository using:

    git clone https://github.com/krockode/sublime-cucumber-completion

Supported Step Definition Formats
---------------------------------

Step definitions can be defined in many languages as the cucumber gherkin
language is parsable in various programming languages.  The [examples](examples)
directory contains cucumber step files in different supported formats
which are tested against.  The `*.expected` files show the completions that will
be generated for sublime projects of these directories.

Specifically this has been tested and works for the examples found in:
* [cucumber/cucumber][2] with the exception of the following:
    * i18n - languages other than the English are not supported yet
    * python - steps defined in python are not suppoerted yet
    * v8 - steps defined in javascript are not supported yet
* groovy examples in [cucumber/cucumber-jvm][3]

Support for steps defined in different language types is planned including
python, javascript as well as Java and other JVM based languages.

TODO
----

* Support more languages

[1]: http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory
[2]: https://github.com/cucumber/cucumber
[3]: https://github.com/cucumber/cucumber-jvm
