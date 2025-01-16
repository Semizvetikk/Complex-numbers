import unittest
from rational import Rational
from complex import Complex

class TestComplex(unittest.TestCase):
    def test_add(self):
        c1 = Complex(Rational(1, 2), Rational(3, 4))
        c2 = Complex(Rational(2, 3), Rational(4, 5))
        result = c1 + c2
        self.assertEqual(str(result), "(1.1666666666666667 + 1.55i)")

        # Сложение с int
        result = c1 + 2
        self.assertEqual(str(result), "(2.5 + 0.75i)")

    def test_sub(self):
        c1 = Complex(Rational(1, 2), Rational(3, 4))
        c2 = Complex(Rational(2, 3), Rational(4, 5))
        result = c1 - c2
        self.assertEqual(str(result), "(-0.16666666666666666 - 0.05i)")

        # Вычитание int
        result = c1 - 1
        self.assertEqual(str(result), "(-0.5 + 0.75i)")

    def test_mul(self):
        c1 = Complex(Rational(1, 2), Rational(3, 4))
        c2 = Complex(Rational(2, 3), Rational(4, 5))
        result = c1 * c2
        self.assertEqual(str(result), "(-0.26666666666666666 + 0.9i)")

        # Умножение на int
        result = c1 * 2
        self.assertEqual(str(result), "(1.0 + 1.5i)")

    def test_truediv(self):
        c1 = Complex(Rational(1, 2), Rational(3, 4))
        c2 = Complex(Rational(2, 3), Rational(4, 5))
        result = c1 / c2
        self.assertEqual(str(result), "(0.860655737704918 + 0.09221311475409837i)")

        # Деление на int
        result = c1 / 2
        self.assertEqual(str(result), "(0.25 + 0.375i)")

    def test_truediv_by_zero(self):
        c1 = Complex(Rational(1, 2), Rational(3, 4))
        c2 = Complex(0, 0)
        with self.assertRaises(ZeroDivisionError):
            c1 / c2

        # Деление на ноль (скаляр)
        with self.assertRaises(ZeroDivisionError):
            c1 / 0

    def test_pow(self):
        c = Complex(Rational(1, 2), Rational(3, 4))
        result = c ** 2
        self.assertEqual(str(result), "(-0.3125 + 0.75i)")

        # Отрицательная степень
        result = c ** -2
        self.assertEqual(str(result), "(-0.019201316803170883 - 2.2945171878600856i)")

    def test_abs(self):
        c = Complex(Rational(3, 4), Rational(4, 5))
        result = c.abs()
        self.assertAlmostEqual(result, 1.09658560997, places=6)

    def test_arg(self):
        c = Complex(Rational(1, 2), Rational(3, 4))
        result = c.arg()
        self.assertAlmostEqual(result, 0.982793723, places=6)

    def test_eq(self):
        c1 = Complex(Rational(1, 2), Rational(3, 4))
        c2 = Complex(Rational(1, 2), Rational(3, 4))
        self.assertTrue(c1 == c2)

        c3 = Complex(Rational(2, 3), Rational(4, 5))
        self.assertFalse(c1 == c3)

    def test_neg(self):
        c = Complex(Rational(1, 2), Rational(3, 4))
        result = -c
        self.assertEqual(str(result), "(-0.5 - 0.75i)")

    def test_add_large_numbers(self):
        c1 = Complex(10 ** 6, 10 ** 6)
        c2 = Complex(2 * 10 ** 6, 3 * 10 ** 6)
        result = c1 + c2
        self.assertEqual(str(result), "(3000000.0 + 4000000.0i)")

    def test_sub_large_numbers(self):
        c1 = Complex(5 * 10 ** 6, 4 * 10 ** 6)
        c2 = Complex(2 * 10 ** 6, 1 * 10 ** 6)
        result = c1 - c2
        self.assertEqual(str(result), "(3000000.0 + 3000000.0i)")

    def test_mul_large_numbers(self):
        c1 = Complex(10 ** 6, 2 * 10 ** 6)
        c2 = Complex(3 * 10 ** 6, 4 * 10 ** 6)
        result = c1 * c2
        self.assertEqual(str(result), "(-5000000000000.0 + 10000000000000.0i)")

    def test_truediv_large_numbers(self):
        c1 = Complex(10 ** 6, 2 * 10 ** 6)
        c2 = Complex(2 * 10 ** 6, 1 * 10 ** 6)
        result = c1 / c2
        self.assertEqual(str(result), "(0.8 + 0.6i)")

    def test_pow_large_numbers(self):
        c = Complex(10 ** 3, 2 * 10 ** 3)
        result = c ** 2
        self.assertEqual(str(result), "(-3000000.0 + 4000000.0i)")

    def test_abs_large_numbers(self):
        c = Complex(3 * 10 ** 6, 4 * 10 ** 6)
        result = c.abs()
        self.assertAlmostEqual(result, 5 * 10 ** 6, places=6)

    def test_neg_large_numbers(self):
        c = Complex(10 ** 6, 2 * 10 ** 6)
        result = -c
        self.assertEqual(str(result), "(-1000000.0 - 2000000.0i)")

    def test_very_large_numbers(self):
        # Очень большие числа
        c1 = Complex(10 ** 100, 10 ** 100)
        c2 = Complex(10 ** 50, 10 ** 50)
        result = c1 + c2
        self.assertEqual(str(result), f"(1e+100 + 1e+100i)")

        result = c1 * c2
        self.assertEqual(str(result), "(0.0 + 2e+150i)")
