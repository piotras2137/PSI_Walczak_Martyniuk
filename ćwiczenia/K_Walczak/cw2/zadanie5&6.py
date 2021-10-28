# Kacper Walczak 155621
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


class ScienceCalculator(Calculator):
    pass

    def potega(self):
        return pow(self.a, self.b)


liczby = Calculator(10, 5)
liczby2 = ScienceCalculator(2, 3)

print(liczby.add())
print(liczby.difference())
print(liczby.multiply())
print(liczby.divide())

print(liczby2.potega())
print(liczby2.multiply())
