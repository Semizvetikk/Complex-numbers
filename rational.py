from fractions import Fraction

class Rational:
    def __init__(self, n: int, m: int):
        self.__numerator = n
        self.__denominator = m

    #getter
    @property
    def numerator(self):
        return self.__numerator

    #setter
    @numerator.setter
    def numerator(self, value: int):
        if isinstance(value, int):
            self.__numerator = value
        elif isinstance(value, Rational):
            self.__numerator = value.numerator
        else:
            raise ValueError("Numerator must be an integer or Rational")

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value: int):
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

    # сокращение дроби
    def reduce(self):
        # Сокращение дроби
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a


        numerator = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
        denominator = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator

        common_divisor = gcd(numerator, denominator)

        # сокращаем дробь
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

    # сложение
    def __add__(self, other):
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

    # вычитание
    def __sub__(self, other):
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

    # умножение
    def __mul__(self, other):
        if isinstance(other, Rational):
            # убедимся, что числители и знаменатели — целые числа
            numerator1 = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
            denominator1 = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator
            numerator2 = other.numerator if isinstance(other.numerator, int) else other.numerator.numerator
            denominator2 = other.denominator if isinstance(other.denominator, int) else other.denominator.numerator

            # выполняем умножение
            new_numerator = numerator1 * numerator2
            new_denominator = denominator1 * denominator2

            # создаем новую дробь и сокращаем её
            r = Rational(new_numerator, new_denominator)
            r.reduce()
            return r
        elif isinstance(other, int):
            # убедимся, что числитель и знаменатель — целые числа
            numerator = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
            denominator = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator

            # выполняем умножение
            new_numerator = numerator * other
            new_denominator = denominator

            # создаем новую дробь и сокращаем её
            r = Rational(new_numerator, new_denominator)
            r.reduce()
            return r
        else:
            raise TypeError("Unsupported operand type")

    # деление
    def __truediv__(self, other):
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


    # равенство дробей
    def __eq__(self, other):
        if isinstance(other, Rational):  # проверка на соответствие типов(other это тип Rational)
            return (self.numerator * other.denominator) == (self.denominator * other.numerator)
        elif isinstance(other, int):
            return self.numerator == (other * self.denominator)
        else:
            raise TypeError("other operand must be an integer or Rational")

    # неравенство дробей
    def __ne__(self, other):
        if not isinstance(other, Rational | int):
            raise TypeError("other operand must be an integer or Rational")
        return not self == other

    # сложение с присваиванием
    def __iadd__(self, other):
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

    # вычитание с присваиванием
    def __isub__(self, other):
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

    # умножение с присваиванием
    def __imul__(self, other):
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

    # деление с присваиванием
    def __itruediv__(self, other):
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

    # унарный минус
    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    # возведение в степень
    def __pow__(self, other: int | None):
        if other < 0:
            return Rational(self.denominator ** (other), self.numerator ** (other))
        elif other > 0:
            return Rational(self.numerator ** (abs(other)), self.denominator ** (abs(other)))
        else:
            return Rational(1,1)


    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __str__(self):
        # убедимся, что числитель и знаменатель — целые числа
        numerator = self.__numerator if isinstance(self.__numerator, int) else self.__numerator.numerator
        denominator = self.__denominator if isinstance(self.__denominator, int) else self.__denominator.numerator

        # выполняем деление и округляем результат
        result = numerator / denominator
        return str(round(result, 10))

    def __float__(self):
        numerator = self.numerator if isinstance(self.numerator, int) else self.numerator.numerator
        denominator = self.denominator if isinstance(self.denominator, int) else self.denominator.numerator
        return numerator / denominator

    @staticmethod
    def from_float(value: float):
        # преобразуем float в Fraction, а затем в Rational
        frac = Fraction(value).limit_denominator()  # преобразуем float в Fraction
        return Rational(frac.numerator, frac.denominator)  # возвращаем Rational


    def __repr__(self):
        return f"Rational({self.__numerator}, {self.__denominator})"

    def print_fraction(self):
        return f"Rational number: {self.__numerator} / {self.__denominator}"
