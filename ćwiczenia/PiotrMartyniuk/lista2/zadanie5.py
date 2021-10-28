import math

class Calculator:

    def add(self, x, y):
        self.x = x
        self.y = y
        a = self.x + self.y
        return a

    def difference(self, x, y):
        self.x = x
        self.y = y
        a = self.x - self.y
        return a

    def multiply(self, x, y):
        self.x = x
        self.y = y
        a = self.x * self.y
        return a

    def divide(self, x, y):
        self.x = x
        self.y = y

        if (y == 0):
            a = "Operation forbidden, can't divide by 0."
        else:
            a = self.x / self.y

        return a


c = Calculator()
print(c.add(1, 3))
print(c.difference(6, 2))
print(c.multiply(2, 5))
print(c.divide(9, 3))