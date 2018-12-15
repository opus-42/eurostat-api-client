import unittest
from src.utils.property_decorators import property_is_boolean, \
    property_is_int, property_is_string


class TestBooleanDecorator(unittest.TestCase):
    """Unit test for the Boolean property decorator."""

    def test_value_error(self):
        class SomeObject(object):
            def __init__(self, value):
                self.value = value

            @property
            def value(self):
                return self._value

            @value.setter
            @property_is_boolean
            def value(self, value):
                self._value = value

        self.assertRaises(ValueError, SomeObject, 3)
        self.assertRaises(ValueError, SomeObject, 'string')

    def test_value_assignation(self):
        class SomeObject(object):
            def __init__(self, value):
                self.value = value

            @property
            def value(self):
                return self._value

            @value.setter
            @property_is_boolean
            def value(self, value):
                self._value = value

        some_object = SomeObject(True)
        self.assertEqual(bool(some_object.value), True)


class TestStringDecorator(unittest.TestCase):
    """Unit test for the String property decorator."""

    def test_value_error(self):
        class SomeObject(object):
            def __init__(self, value):
                self.value = value

            @property
            def value(self):
                return self._value

            @value.setter
            @property_is_string
            def value(self, value):
                self._value = value

        self.assertRaises(ValueError, SomeObject, 3)
        self.assertRaises(ValueError, SomeObject, True)

    def test_value_assignation(self):
        class SomeObject(object):
            def __init__(self, value):
                self.value = value

            @property
            def value(self):
                return self._value

            @value.setter
            @property_is_string
            def value(self, value):
                self._value = value

        some_object = SomeObject('String')
        self.assertEqual(str(some_object.value), 'String')


class TestIntegerDecorator(unittest.TestCase):
    """Unit test for the Integer property decorator."""

    def test_value_error(self):
        class SomeObject(object):
            def __init__(self, value):
                self.value = value

            @property
            def value(self):
                return self._value

            @value.setter
            @property_is_int()
            def value(self, value):
                self._value = value

        self.assertRaises(ValueError, SomeObject, True)
        self.assertRaises(ValueError, SomeObject, 'string')

    def test_value_assignation(self):
        class SomeObject(object):
            def __init__(self, value):
                self.value = value

            @property
            def value(self):
                return self._value

            @value.setter
            @property_is_int()
            def value(self, value):
                self._value = value

        some_object = SomeObject(0)
        self.assertEqual(int(some_object.value), 0)
        some_object = SomeObject(-100)
        self.assertEqual(int(some_object.value), -100)
        some_object = SomeObject(100)
        self.assertEqual(int(some_object.value), 100)

    def test_range_limitation(self):
            class SomeObject(object):
                def __init__(self, value):
                    self.value = value

                @property
                def value(self):
                    return self._value

                @value.setter
                @property_is_int((0, 1000))
                def value(self, value):
                    self._value = value

            some_object = SomeObject(500)
            self.assertEqual(int(some_object.value), 500)
            self.assertRaises(ValueError, SomeObject, 1001)
            self.assertRaises(ValueError, SomeObject, -1)
