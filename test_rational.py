from rational import Rational
import unittest

class TestRational(unittest.TestCase):
    def test_init(self):
        r = Rational(1, 2)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 2)

    def test_add(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 + r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 1)

    def test_sub(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        r3 = r1 - r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 4)

    def test_mul(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 * r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 4)

    def test_truediv(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r3 = r1 / r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 1)

    def test_truediv_by_zero(self):
        r1 = Rational(1, 2)
        r2 = Rational(0, 1)
        with self.assertRaises(ZeroDivisionError):
            r1 / r2

    def test_eq(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        self.assertTrue(r1 == r2)

    def test_ne(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        self.assertTrue(r1 != r2)

    def test_iadd(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r1 += r2
        self.assertEqual(r1.numerator, 1)
        self.assertEqual(r1.denominator, 1)

    def test_isub(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        r1 -= r2
        self.assertEqual(r1.numerator, 1)
        self.assertEqual(r1.denominator, 4)

    def test_imul(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r1 *= r2
        self.assertEqual(r1.numerator, 1)
        self.assertEqual(r1.denominator, 4)

    def test_itruediv(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 2)
        r1 /= r2
        self.assertEqual(r1.numerator, 1)
        self.assertEqual(r1.denominator, 1)

    def test_itruediv_by_zero(self):
        r1 = Rational(1, 2)
        r2 = Rational(0, 1)
        with self.assertRaises(ZeroDivisionError):
            r1 /= r2

    def test_neg(self):
        r1 = Rational(1, 2)
        r2 = -r1
        self.assertEqual(r2.numerator, -1)
        self.assertEqual(r2.denominator, 2)

    def test_pow(self):
        r1 = Rational(1, 2)
        r2 = r1 ** 2
        self.assertEqual(r2.numerator, 1)
        self.assertEqual(r2.denominator, 4)

    def test_abs(self):
        r1 = Rational(-1, 2)
        r2 = abs(r1)
        self.assertEqual(r2.numerator, 1)
        self.assertEqual(r2.denominator, 2)

    def test_str(self):
        r1 = Rational(1, 2)
        self.assertEqual(str(r1), "0.5")

    def test_float(self):
        r1 = Rational(1, 2)
        self.assertEqual(float(r1), 0.5)

    def test_repr(self):
        r1 = Rational(1, 2)
        self.assertEqual(repr(r1), "Rational(1, 2)")

    def test_add_large_numbers(self):
        r1 = Rational(123456789, 987654321)
        r2 = Rational(987654321, 123456789)
        result = r1 + r2
        self.assertEqual(result.numerator, 12230896747409402)
        self.assertEqual(result.denominator, 1505341124847349)

    def test_divide_large_numbers(self):
        r1 = Rational(123456789, 987654321)
        r2 = Rational(987654321, 123456789)
        result = r1 / r2
        self.assertEqual(result.numerator, 188167638891241)
        self.assertEqual(result.denominator, 12042729108518161)

    def test_compare_large_numbers(self):
        r1 = Rational(123456789, 987654321)
        r2 = Rational(987654321, 123456789)
        self.assertTrue(r1 != r2)

    def test_very_large_numbers(self):
        r1 = Rational(10 ** 100, 10 ** 50)
        r2 = Rational(10 ** 50, 10 ** 100)
        result = r1 * r2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_very_large_numbers_division(self):
        r1 = Rational(10 ** 100, 10 ** 50)
        r2 = Rational(10 ** 50, 10 ** 100)
        result = r1 / r2
        self.assertEqual(result.numerator, 10**100)
        self.assertEqual(result.denominator, 1)

    def test_overflow(self):
        r1 = Rational(10 ** 1000, 10 ** 500)
        r2 = Rational(10 ** 500, 10 ** 1000)
        result = r1 * r2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)
