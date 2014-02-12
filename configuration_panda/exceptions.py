"""
Custom exceptions for ConfigurationPanda.

"""


class ConfigurationPandaError(Exception):
    """
    Base exception class for ConfigurationPanda Errors.
    """


class DuplicateJSONFile(ConfigurationPandaError):
    """
    Error to raise when an attempt is made to load a configuration file
    with the same names as a previously loaded file.

    """


class MalformedJSONFile(ConfigurationPandaError):
    """
    Error to raise when an attempt is made to load a configuration
    file contained malformed JSON.

    """


class ExistingEnvironmentVariable(ConfigurationPandaError):
    """
    Error to raise when an existing environment variable prevents a
    program operation from succeeding.

    """


class InvalidParameter(ConfigurationPandaError):
    """
    Error to raise when an error arises from the use of invalid
    input provided by the client.

    """

