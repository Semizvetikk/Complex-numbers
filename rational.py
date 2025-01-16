from fractions import Fraction

class Rational:
    """
    Класс для работы с рациональными числами.
    Атрибуты:
        __numerator (int): Числитель дроби
        __denominator (int): Знаменатель дроби
    """
    def __init__(self, n: int, m: int):
        """
        Инициализация дроби с заданным числителем и знаменателем.

        Аргументы:
            n (int): Числитель дроби.
            m (int): Знаменатель дроби.
        """
        self.__numerator = n
        self.__denominator = m

    #getter
    @property
    def numerator(self):
        """
        Возвращает числитель дроби.
        :return:
            int: Числитель дроби
        """
        return self.__numerator

    #setter
    @numerator.setter
    def numerator(self, value: int):
        """
        Устанавливает числитель дроби.
        :param value: Новое значение числителя. Может быть целым числом или объектом Rational.
        Исключения:
            ValueError: Если значение не является целым числом или объектом Rational.
        """
        if isinstance(value, int):
            self.__numerator = value
        elif isinstance(value, Rational):
            self.__numerator = value.numerator
        else:
            raise ValueError("Numerator must be an integer or Rational")

    @property
    def denominator(self):
        """
        Возвращает знаменатель дроби.
        :return:
            int: Знаменатель дроби
        """
        return self.__denominator

    @denominator.setter
    def denominator(self, value: int):
        """
        Устанавливает знаменатель дроби.
        :param value: Новое значение знаменателя. Может быть целым числом или объектом Rational.
        Исключения:
            ValueError: Если значение не является целым числом или объектом Rational, или если знаменатель равен нулю.
        """
        if isinstance(value, int):
            if value == 0:
                raise ValueError("Denominator cannot be zero.")
            self.__denominator = value
        elif isinstance(value, Rational):
            self.__denominator = value.denominator
        else:
            raise ValueError("Denominator must be an integer or Rational.")
        if value != 0:
            self.__denominator = value
        else:
            raise ValueError("Division by zero")


    def reduce(self):
        """
        Функция сокращает дробь до несократимого вида.
        Метод находит наибольший общий делитель (НОД) числителя и знаменателя
        и делит их на него, чтобы сократить дробь.
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a


        numerator = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
        denominator = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator

        common_divisor = gcd(numerator, denominator)


        if isinstance(self.numerator, int):
            self.numerator = self.numerator // common_divisor
        else:
            self.numerator = Rational(self.numerator.numerator // common_divisor, self.numerator.denominator)

        if isinstance(self.denominator, int):
            self.denominator = self.denominator // common_divisor
        else:
            self.denominator = Rational(self.denominator.numerator // common_divisor, self.denominator.denominator)
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1


    def __add__(self, other):
        """
        Функция сложения рационального числа с другим числом (дробью или целым числом).
            :param other: Другое рациональное число.
            :return:
                Сумма двух рациональных чисел.
        """
        if isinstance(other, Rational): # проверка на соответствие типов (other это тип Rational)
            r = Rational(self.numerator * other.denominator + self.denominator * other.numerator,
                         self.denominator * other.denominator)
            r.reduce()
            return r
        elif isinstance(other, int):
            return Rational(self.numerator + other * self.denominator,
                            self.denominator)
        else:
            raise TypeError("Denominator must be an integer or Rational")


    def __sub__(self, other):
        """
        Функция вычитания другого числа (дроби или целого числа) из рационального числа.
        :param other: Другое рациональное число.
        :return:
            Разность двух рациональных чисел.
        """
        if isinstance(other, Rational):
            r = Rational(self.numerator * other.denominator - self.denominator * other.numerator,
                         self.denominator * other.denominator)
            r.reduce()
            return r
        elif isinstance(other, int):
            return Rational(self.numerator - other * self.denominator,
                            self.denominator)
        else:
            raise TypeError("Denominator must be an integer or Rational")


    def __mul__(self, other):
        """
        Функция умножения рационального числа на другое число (другую дробь или целое число).
        :param other: Другое рациональное число.
        :return:
            Новая дробь, представляющая результат умножения.
        """
        if isinstance(other, Rational):
            # убедимся, что числители и знаменатели — целые числа
            numerator1 = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
            denominator1 = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator
            numerator2 = other.numerator if isinstance(other.numerator, int) else other.numerator.numerator
            denominator2 = other.denominator if isinstance(other.denominator, int) else other.denominator.numerator

            new_numerator = numerator1 * numerator2
            new_denominator = denominator1 * denominator2

            r = Rational(new_numerator, new_denominator)
            r.reduce()
            return r
        elif isinstance(other, int):
            numerator = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
            denominator = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator

            new_numerator = numerator * other
            new_denominator = denominator

            r = Rational(new_numerator, new_denominator)
            r.reduce()
            return r
        else:
            raise TypeError("Unsupported operand type")


    def __truediv__(self, other):
        """
        Функция деления текущей дроби на другое число (дробь или целое число).
        :param other: Число, на которое нужно разделить текущую дробь.
        :return:
            Новая дробь, представляющая результат деления.
        """
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            r = Rational(self.numerator * other.denominator, self.denominator * other.numerator)
            r.reduce()
            return r
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Rational(self.numerator, self.denominator * other)
        else:
            raise TypeError("Denominator must be an integer or Rational")


    def __eq__(self, other):
        """
        Функция сравнения двух дробей.
        :param other: Число, с которым нужно сравнить текущую дробь.
        :return:
            bool: True, если дроби равны, иначе False.
        """
        if isinstance(other, Rational):  # проверка на соответствие типов(other это тип Rational)
            return (self.numerator * other.denominator) == (self.denominator * other.numerator)
        elif isinstance(other, int):
            return self.numerator == (other * self.denominator)
        else:
            raise TypeError("other operand must be an integer or Rational")


    def __ne__(self, other):
        """
        Функция проверки на неравенство двух дробей.
        :param other: Число, с которым нужно сравнить текущую дробь.
        :return:
            bool: True, если дроби не равны, иначе False.
        """
        if not isinstance(other, Rational | int):
            raise TypeError("other operand must be an integer or Rational")
        return not self == other


    def __iadd__(self, other):
        """
        Функция сложения с присваиванием текущей дроби с другим числом (дробью или целым числом).
        :param other: Число, которое нужно добавить к текущей дроби.
        :return:
            Rational: Текущая дробь после сложения.
        """
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            self.numerator = new_numerator
            self.denominator = new_denominator
            self.reduce()
            return self
        elif isinstance(other, int):
            new_numerator = self.numerator + other * self.denominator
            self.numerator = new_numerator
            return self
        else:
            raise TypeError("other operand must be an integer or Rational")


    def __isub__(self, other):
        """
        Функция вычитания с присваиванием из текущей дроби другого числа (дроби или целого числа).
        :param other: Число, которое нужно вычесть из текущей дроби.
        :return:
            Rational: Текущая дробь после вычитания.
        """
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            self.numerator = new_numerator
            self.denominator = new_denominator
            self.reduce()
            return self
        elif isinstance(other, int):
            new_numerator = self.numerator - other * self.denominator
            self.numerator = new_numerator
            self.reduce()
            return self
        else:
            raise TypeError("other operand must be an integer or Rational")


    def __imul__(self, other):
        """
        Функция умножения с присваиванием текущей дроби на другое число (дробь или целое число).
        :param other: Число, на которое нужно умножить текущую дробь.
        :return:
            Текущая дробь после умножения.
        """
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            self.numerator = new_numerator
            self.denominator = new_denominator
            self.reduce()
            return self
        elif isinstance(other, int):
            new_numerator = self.numerator * other
            self.numerator = new_numerator
            self.reduce()
            return self
        else:
            raise TypeError("other operand must be an integer or Rational")


    def __itruediv__(self, other):
        """
        Функция деления с присваиванием текущей дроби на другое число (дробь или целое число).
        :param other: Число, на которое нужно разделить текущую дробь.
        :return:
            Текущая дробь после деления.
        """
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            self.numerator = new_numerator
            self.denominator = new_denominator
            self.reduce()
            return self
        elif isinstance(other, int):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            new_denominator = self.denominator * other
            self.denominator = new_denominator
            self.reduce()
            return self
        else:
            raise TypeError("other operand must be an integer or Rational")


    def __neg__(self):
        """
        Функция получения противоположного числа.
        :return:
            Rational: Противоположное число.
        """
        return Rational(-self.numerator, self.denominator)


    def __pow__(self, other: int | None):
        """
        Функция возведения дроби в степень.
        :param other(int): Степень, в которую нужно возвести дробь.
        :return:
            Новая дробь, представляющая результат возведения в степень.
        """
        if other < 0:
            return Rational(self.denominator ** (other), self.numerator ** (other))
        elif other > 0:
            return Rational(self.numerator ** (abs(other)), self.denominator ** (abs(other)))
        else:
            return Rational(1,1)


    def __abs__(self):
        """
        Функция получения абсолютного значения дроби.
        :return:
            Новая дробь, представляющая абсолютное значение текущей дроби.
        """
        return Rational(abs(self.numerator), abs(self.denominator))

    def __str__(self):
        """
        Функция получения строкового представления дроби в виде десятичного числа.
        :return:
            Строковое представление дроби, округленное до 10 знаков после запятой.
        """
        numerator = self.__numerator if isinstance(self.__numerator, int) else self.__numerator.numerator
        denominator = self.__denominator if isinstance(self.__denominator, int) else self.__denominator.numerator

        result = numerator / denominator
        return str(round(result, 10))

    def __float__(self):
        """
        Функция получения десятичного представления дроби.
        :return:
            float: Десятичное представление дроби.
        """
        numerator = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
        denominator = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator
        return numerator / denominator

    @staticmethod
    def from_float(value: float):
        """
        Функция получения Rational из float.
        :param value: float, из которого нужно получить Rational.
        :return:
            Rational: Rational, полученный из float.
        """
        frac = Fraction(value).limit_denominator()
        return Rational(frac.numerator, frac.denominator)


    def __repr__(self):
        """
        Функция получения строкового представления дроби.
        :return:
            str: Строковое представление объекта Rational.
        """
        return f"Rational({self.__numerator}, {self.__denominator})"

    def print_fraction(self):
        """
        Возвращает строковое представление дроби в виде "числитель / знаменатель".
        :return:
            str: Строковое представление дроби в виде "числитель / знаменатель".
        """
        return f"Rational number: {self.__numerator} / {self.__denominator}"
