from zadanie5 import *
import math

class ScienceCalculator(Calculator):

    def exponentiation(self, x, y):
        self.x = x
        self.y = y

        if (y == 0 and x == 0):
            a = "Operation forbidden, 0^0 is an unmarked symbol."
        else:
            a = self.x ** self.y

        return a

    def factorial(self, x):
        self.x = x
        a = math.factorial(self.x)
        return a


s = ScienceCalculator()
print(s.exponentiation(5, 0))
print(s.factorial(3)) # oifowa