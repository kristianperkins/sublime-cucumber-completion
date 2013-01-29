Cucumber Completion
===================

Sublime plugin to auto complete Cucumber step definitions.

Installation
------------

While inside the Sublime Packages directory, clone the theme repository using:

    git clone https://github.com/krockode/cucumber-completion


Supported Step Definition Formats
---------------------------------

Step definitions can be defined in many languages as the cucumber gherkin
language is parsable in various programming languages.

Autocompletion has been tested and works for the examples found in:
* [cucumber][1] with the exception of the following:
    * i18n - languages other than the English are not supported yet
    * python - steps defined in python are not suppoerted yet
    * v8 - steps defined in javascript are not supported yet
* groovy examples in [cucumber-jvm][2]

Support for steps defined in different language types is planned including
python, javascript as well as Java and other JVM based languages.

TODO
----

Supported formats in different programming languages defined via tests.

[1]: https://github.com/cucumber/cucumber
[2]: https://github.com/cucumber/cucumber-jvm
