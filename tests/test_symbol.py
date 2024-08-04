from unittest import TestCase

from pythonz_symbol import symbol


class TestSymbol(TestCase):
    def test_symbol_is_always_the_same(self):
        test = symbol('test')

        def f(a=test):
            return a is test

        # symbol is not a singleton for the same name
        self.assertTrue(f(test))

    def test_symbol_not_singleton(self):
        test = symbol('test')
        test2 = symbol('test')

        # symbol is not a singleton for the same name
        self.assertIsNot(test, test2)
