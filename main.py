import decimal
from math import factorial

n = int(input())

def chudnovsky(n):
   decimal.getcontext().prec = n + 1
   pi = decimal.Decimal(0)
   k = 0
   while k < n:
       pi += (decimal.Decimal(-1) ** k) * (decimal.Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (
                    13591409 + 545140134 * k) / (640320 ** (3 * k)))
       k += 1
   pi = pi * decimal.Decimal(10005).sqrt() / 4270934400
   pi = pi ** (-1)
   return pi


print(chudnovsky(n))

