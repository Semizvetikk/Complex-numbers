from rational import Rational
from math import atan2, sqrt

class Complex:
    def __init__(self, real, imag=None):
        if imag is None:  # если imag не указан, считаем, что real — это вещественное число, а imag = 0
            if isinstance(real, (int, float)):
                self.real = Rational.from_float(float(real)) if isinstance(real, float) else Rational(real, 1)
                self.imag = Rational(0, 1)
            elif isinstance(real, Rational):
                self.real = real
                self.imag = Rational(0, 1)
            else:
                raise TypeError("real must be Rational, int, or float")
        else:
            # если imag указан, обрабатываем real и imag как обычно
            self.real = Rational(int(real), 1) if isinstance(real, int) else Rational.from_float(float(real))
            self.imag = Rational(int(imag), 1) if isinstance(imag, int) else Rational.from_float(float(imag))

    # Геттер для действительной части
    @property
    def real(self):
        return self.__real

    # Сеттер для действительной части
    @real.setter
    def real(self, value):
        if isinstance(value, Rational):
            self.__real = value
        elif isinstance(value, (int, float)):
            self.__real = Rational.from_float(float(value)) if isinstance(value, float) else Rational(value, 1)
        else:
            raise TypeError("real must be Rational, int or float")

    # Геттер для мнимой части
    @property
    def imag(self):
        return self.__imag

    # Сеттер для мнимой части
    @imag.setter
    def imag(self, value):
        if isinstance(value, Rational):
            self.__imag = value
        elif isinstance(value, (int, float)):
            self.__imag = Rational.from_float(float(value)) if isinstance(value, float) else Rational(value, 1)
        else:
            raise TypeError("imag must be Rational, int or float")

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (Rational, int, float)):
            return Complex(self.real + other, self.imag)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (Rational, int, float)):
            return Complex(self.real - other, self.imag)
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, Complex):
            # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        # Умножение на скаляр (int или float)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)

        # Умножение на Rational
        elif isinstance(other, Rational):
            scalar = float(other.numerator) / float(other.denominator)
            return Complex(self.real * scalar, self.imag * scalar)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real ** 2 + other.imag ** 2
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero complex number")
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)
        elif isinstance(other, (Rational, int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero scalar")
            return Complex(self.real / other, self.imag / other)
        else:
            raise TypeError("Unsupported operand type")


    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        elif isinstance(other, (Rational, int, float)):
            return self.real == other and self.imag == Rational(0, 1)
        else:
            raise TypeError("Unsupported operand type")

    def __ne__(self, other):
        return not self == other

    def __iadd__(self, other):
        if isinstance(other, Complex):
            self.real += other.real
            self.imag += other.imag
        elif isinstance(other, (Rational, int, float)):
            self.real += other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __isub__(self, other):
        if isinstance(other, Complex):
            self.real -= other.real
            self.imag -= other.imag
        elif isinstance(other, (Rational, int, float)):
            self.real -= other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __imul__(self, other):
        if isinstance(other, Complex):
            new_real = self.real * other.real - self.imag * other.imag
            new_imag = self.real * other.imag + self.imag * other.real
            self.real = new_real
            self.imag = new_imag
        elif isinstance(other, (Rational, int, float)):
            if isinstance(other, (int, float)):
                other = Rational(int(other), 1) if isinstance(other, int) else Rational.from_float(float(other))
            self.real *= other
            self.imag *= other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __itruediv__(self, other):
        if isinstance(other, Complex):
            if other.real == 0 and other.imag == 0:
                raise ZeroDivisionError("Cannot divide by zero complex number")
            denominator = other.real ** 2 + other.imag ** 2
            if denominator == 0:
                raise ValueError("Cannot divide by zero")
            new_real = (self.real * other.real + self.imag * other.imag) / denominator
            new_imag = (self.imag * other.real - self.real * other.imag) / denominator
            self.real = new_real
            self.imag = new_imag
        elif isinstance(other, (Rational, int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            self.real /= other
            self.imag /= other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __pow__(self, other: int):
        if not isinstance(other, int):
            raise TypeError("Exponent must be an integer")
        if other < 0:
            return (self.inverse()) ** (-other)
        elif other == 0:
            return Complex(1, 0)
        elif other == 1:
            return self
        else:
            result = Complex(1, 0)
            base = self
            while other > 0:
                if other % 2 == 1:
                    result *= base
                base *= base
                other //= 2
            return result

    def inverse(self):
        denominator = self.real * self.real + self.imag * self.imag
        if denominator == 0:
            raise ValueError("Cannot invert zero complex number")
        return Complex(self.real / denominator, -self.imag / denominator)

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __str__(self):
        real_float = float(self.real)
        imag_float = float(self.imag)
        if imag_float >= 0:
            return f"({real_float} + {imag_float}i)"
        else:
            return f"({real_float} - {abs(imag_float)}i)"

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def abs(self) -> float:
        return sqrt(float(self.real) ** 2 + float(self.imag) ** 2)

    def arg(self) -> float:
        real_float = float(self.real)
        imag_float = float(self.imag)
        return atan2(imag_float, real_float)