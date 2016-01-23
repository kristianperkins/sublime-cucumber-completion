Cucumber Completion
===================

[![Build Status](https://travis-ci.org/krockode/sublime-cucumber-completion.png?branch=master)](https://travis-ci.org/krockode/sublime-cucumber-completion)
[![Coverage
Status](https://coveralls.io/repos/krockode/sublime-cucumber-completion/badge.png?branch=master)](https://coveralls.io/r/krockode/sublime-cucumber-completion?branch=master)

[Plugin Information][5] on [packagecontrol.io][4].

Sublime plugin to auto complete Cucumber step definitions.

Installation
------------

### Using Sublime Package Control ###

If you are using Will Bond's excellent [Sublime Package Control][4], you can easily
install Cucumber Completion via the `Package Control: Install Package` menu item.
This package is listed as `Cucumber Completion` in the packages list.

### Using Git ###

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
    * i18n - languages other than the English are not supported
    * python - steps defined in python are not suppoerted
    * v8 - steps defined in javascript are not supported
* groovy examples in [cucumber/cucumber-jvm][3]

Support for steps defined in different language types is planned including
python, javascript as well as Java and other JVM based languages. 

There are many formats so if you would like a specific flavour implemented
please submit an issue for your flavour and/or a pull request with
[an example in the examples directory](examples) of your step definition format.


More Languages
--------------

Cucumber is implemented in many languages and this plugin only supports a couple
of implementations.  If you would like to see more languages supported, create
an issue or submit a pull request.

[1]: http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory
[2]: https://github.com/cucumber/cucumber
[3]: https://github.com/cucumber/cucumber-jvm
[4]: https://packagecontrol.io
[5]: https://packagecontrol.io/packages/Cucumber%20Completion
