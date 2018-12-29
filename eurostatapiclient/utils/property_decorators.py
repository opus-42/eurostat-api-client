"""
    Define a set of property decorators that allow to quickly
    set the type of a property. It performs the necessary checks
    and raise an error in case the passed to setter is incorrect.
    This code is largely inspired from :
    https://github.com/tableau/server-client-python.git
    Check out the original code at
    "./tableauserverclient/models/property_decorators.py"
    in the repository
"""


from functools import wraps
from datetime import datetime


def property_is_boolean(func):
    """
    Define property as a Boolean.
    and raises a ValueError when value passed to the setter
    is not a Boolean.
    """
    @wraps(func)
    def wrapper(self, value):
        if not isinstance(value, bool):
            error = "Boolean expected for {0} flag.".format(func.__name__)
            raise ValueError(error)
        return func(self, value)
    return wrapper


def property_is_string(func):
    """
    Define property as a String.
    and raises a ValueError when value passed to the setter
    is not a String.
    """
    @wraps(func)
    def wrapper(self, value):
        if not isinstance(value, str):
            error = "String expected for {0} flag.".format(func.__name__)
            raise ValueError(error)
        return func(self, value)
    return wrapper


def property_is_datetime(func):
    """
    Define property as a Datetime.
    and raises a ValueError when value passed to the setter
    is not a Datetime.
    """
    @wraps(func)
    def wrapper(self, value):
        if not isinstance(value, datetime):
            error = "Datetime expected for {0} flag.".format(func.__name__)
            raise ValueError(error)
        return func(self, value)
    return wrapper


def property_is_int(range=None, allowed=None):
    """
    Takes a range of ints and a list of exemptions
    to check against when setting a property on a model.
    The range is a tuple of (min, max) and the allowed list
    (empty by default) allows values outside that range.
    This is useful for when we use sentinel valuesself.
    Example: Revisions allow a range of 2-10000,
    but use -1 as a sentinel for 'unlimited'.
    """

    if allowed is None:
        allowed = ()  # Empty tuple for fast no-op testing.

    def property_type_decorator(func):
        @wraps(func)
        def wrapper(self, value):
            error = "Invalid priority defined: {}.".format(value)

            if range is None:
                if isinstance(value, int) and not isinstance(value, bool):
                    return func(self, value)
                else:
                    raise ValueError(error)

            min, max = range

            if (value < min or value > max) and (value not in allowed):
                raise ValueError(error)

            return func(self, value)
        return wrapper
    return property_type_decorator
