from unittest import TestCase

from pythonz_enum import Enum, case, Maybe, Result, UnwrapNothingError


class TestEnum(TestCase):
    def test_enum(self):
        class MyEnum(Enum):
            A = case("A", ...)
            B = case("B", ...)
            C = case("C", ...)

        a = MyEnum.A(1)

        self.assertEqual(a.match({
            MyEnum.A: lambda val: val + 1,
            MyEnum.B: lambda val: val,
            MyEnum.C: lambda val: val - 1,
        }), 2)

    def test_maybe(self):
        a = Maybe.just(3)
        b = Maybe.nothing()

        self.assertEqual(a.unwrap(), 3)
        self.assertRaises(UnwrapNothingError, b.unwrap)

    def test_result(self):
        a = Result.ok(3)
        b = Result.err(RuntimeError("test"))

        self.assertEqual(a.unwrap(), 3)
        self.assertRaises(RuntimeError, b.unwrap)
