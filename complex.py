from rational import Rational
from math import atan2, sqrt

class Complex:
    """
    Класс для работы с комплексными числами.
    Атрибуты:
        real (Rational): Действительная часть комплексного числа.
        imag (Rational): Мнимая часть комплексного числа.
    """
    def __init__(self, real, imag=None):
        """
        Инициализация комплексного числа.
        :param real: Действительная часть комплексного числа.
        :param imag: Мнимая часть комплексного числа. Если не указана, считается равной 0.
        """
        if imag is None:
            if isinstance(real, (int, float)):
                self.real = Rational.from_float(float(real)) if isinstance(real, float) else Rational(real, 1)
                self.imag = Rational(0, 1)
            elif isinstance(real, Rational):
                self.real = real
                self.imag = Rational(0, 1)
            else:
                raise TypeError("real must be Rational, int, or float")
        else:
            self.real = Rational(int(real), 1) if isinstance(real, int) else Rational.from_float(float(real))
            self.imag = Rational(int(imag), 1) if isinstance(imag, int) else Rational.from_float(float(imag))

    @property
    def real(self):
        """
        :return:
            Rational: Действительная часть комплексного числа.
        """
        return self.__real

    @real.setter
    def real(self, value):
        """
        Устанавливает действительную часть комплексного числа.
        :param value: Новое значение действительной части.
        """
        if isinstance(value, Rational):
            self.__real = value
        elif isinstance(value, (int, float)):
            self.__real = Rational.from_float(float(value)) if isinstance(value, float) else Rational(value, 1)
        else:
            raise TypeError("real must be Rational, int or float")


    @property
    def imag(self):
        """
        :return:
            Rational: Мнимая часть комплексного числа.
        """
        return self.__imag

    @imag.setter
    def imag(self, value):
        """
        Устанавливает мнимую часть комплексного числа.
        :param value: Новое значение мнимой части.
        """
        if isinstance(value, Rational):
            self.__imag = value
        elif isinstance(value, (int, float)):
            self.__imag = Rational.from_float(float(value)) if isinstance(value, float) else Rational(value, 1)
        else:
            raise TypeError("imag must be Rational, int or float")

    def __add__(self, other):
        """
        Функция сложения комплексного числа с другим числом (комплексным, Rational, int или float).
        :param other (Complex | Rational | int | float): Число, которое нужно добавить к текущему комплексному числу.
        :return:
            Complex: Новое комплексное число, представляющее результат сложения.
        """
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (Rational, int, float)):
            return Complex(self.real + other, self.imag)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        """
        Функция вычитания другого числа (комплексного, Rational, int или float) из комплексного числа.
        :param other(Complex | Rational | int | float): Число, которое нужно вычесть из текущего комплексного числа.
        :return:
            Complex: Новое комплексное число, представляющее результат вычитания.
        """
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (Rational, int, float)):
            return Complex(self.real - other, self.imag)
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        """
        Функция умножения комплексного числа на другое число (комплексное, Rational, int или float).
        :param other (Complex | Rational | int | float): Число, на которое нужно умножить текущее комплексное число.
        :return:
            Complex: Новое комплексное число, представляющее результат умножения.
        """
        if isinstance(other, Complex):

            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)

        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)

        elif isinstance(other, Rational):
            scalar = float(other.numerator) / float(other.denominator)
            return Complex(self.real * scalar, self.imag * scalar)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        """
        Функция деления текущего комплексного числа на другое число (комплексное, Rational, int или float).
        :param other(Complex | Rational | int | float): Число, на которое нужно разделить текущее комплексное число.
        :return:
            Complex: Новое комплексное число, представляющее результат деления.
        """
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
        """
        Проверка на равенство комплексного числа с другим числом (комплексным, Rational, int или float).
        :param other (Complex | Rational | int | float): Число, с которым нужно сравнить текущее комплексное число.
        :return:
            bool: True, если числа равны, False в противном случае.
        """
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        elif isinstance(other, (Rational, int, float)):
            return self.real == other and self.imag == Rational(0, 1)
        else:
            raise TypeError("Unsupported operand type")

    def __ne__(self, other):
        """
        Проверка на неравенство текущего комплексного числа с другим числом (комплексным, Rational, int или float).
        :param other (Complex | Rational | int | float): Число, с которым нужно сравнить текущее комплексное число.
        :return:
            bool: True, если числа не равны, иначе False.
        """
        return not self == other

    def __iadd__(self, other):
        """
        Функция сложения с присваиванием текущего комплексного числа с другим числом (комплексным, Rational, int или float).
        :param other(Complex | Rational | int | float): Число, которое нужно добавить к текущему комплексному числу.
        :return:
            Complex: Текущее комплексное число после сложения.
        """
        if isinstance(other, Complex):
            self.real += other.real
            self.imag += other.imag
        elif isinstance(other, (Rational, int, float)):
            self.real += other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __isub__(self, other):
        """
        Функция вычитания с присваиванием текущего комплексного числа с другим числом (комплексным, Rational, int или float).
        :param other(Complex | Rational | int | float): Число, которое нужно вычесть из текущего комплексного числа.
        :return:
            Complex: Текущее комплексное число после вычитания.
        """
        if isinstance(other, Complex):
            self.real -= other.real
            self.imag -= other.imag
        elif isinstance(other, (Rational, int, float)):
            self.real -= other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __imul__(self, other):
        """
        Функция умножения с присваиванием текущего комплексного числа на другое число (комплексное, Rational, int или float).
        :param other(Complex | Rational | int | float): Число, на которое нужно умножить текущее комплексное число.
        :return:
            Complex: Текущее комплексное число после умножения.
        """
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
        """
        Функция деления с присваиванием текущего комплексного числа на другое число (комплексное, Rational, int или float).
        :param other(Complex | Rational | int | float): Число, на которое нужно разделить текущее комплексное число.
        :return:
            Complex: Текущее комплексное число после деления.
        """
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
        """
        Функция возведения текущего комплексного числа в целую степень.
        :param other (int): Степень, в которую нужно возвести комплексное число.
        :return:
            Complex: Новое комплексное число, представляющее результат возведения в степень.
        """
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
        """
        Функция инверсии комплексного числа.
        :return:
            Complex: Обратное комплексное число.
        """
        denominator = self.real * self.real + self.imag * self.imag
        if denominator == 0:
            raise ValueError("Cannot invert zero complex number")
        return Complex(self.real / denominator, -self.imag / denominator)

    def __neg__(self):
        """
        Функция получения противоположного комплексного числа.
        :return:
            Complex: Противоположное значение текущего комплексного числа.
        """
        return Complex(-self.real, -self.imag)

    def __str__(self):
        """
        Функция преобразования комплексного числа в строку.
        :return:
            str: Строковое представление комплексного числа.
        """
        real_float = float(self.real)
        imag_float = float(self.imag)
        if imag_float >= 0:
            return f"({real_float} + {imag_float}i)"
        else:
            return f"({real_float} - {abs(imag_float)}i)"

    def __repr__(self):
        """
        Функция преобразования комплексного числа в строку.
        :return:
            str: Строковое представление комплексного числа.
        """
        return f"Complex({self.real}, {self.imag})"

    def abs(self) -> float:
        """
        Функция вычисления модуля комплексного числа.
        :return:
            float: Модуль комплексного числа.
        """
        return sqrt(float(self.real) ** 2 + float(self.imag) ** 2)

    def arg(self) -> float:
        """
        Функция вычисления аргумента комплексного числа (в радианах).
        :return:
            float: Аргумент комплексного числа.
        """
        real_float = float(self.real)
        imag_float = float(self.imag)
        return atan2(imag_float, real_float)