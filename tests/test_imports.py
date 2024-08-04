import unittest


class TestImports(unittest.TestCase):
    def test_import_pipe(self):
        try:
            from pythonz import pipe
        except ImportError as e:
            self.fail(f"Import pipe failed: {e}")

        a = pipe(5) / range // list
        b = [0, 1, 2, 3, 4]
        self.assertListEqual(a, b)

    def test_import_symbol(self):
        try:
            from pythonz import symbol
        except ImportError as e:
            self.fail(f"Import symbol failed: {e}")

        a = symbol("test")
        self.assertTrue(a)
