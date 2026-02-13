# 10demo.py by Justin Arguijo

import math

print('hello, again') # greeting
"""
This is a
multi-line
comment
"""

print(1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3)
print(5//2)
print(5%2)
print(5*(2+1))

print(abs(21))
print(pow(2, 3))
print(round(12345, ndigits=3))

print(math.pow(2,3))
print(math.sqrt(2))
print(math.log(2))
print('ascii values:')
print('A = 65, a = 97')

print(0.1 * 1)
print(0.1 * 3)

a = 3                      #side of triangle
b = 4                      #side of triangle
c = math.sqrt(a**2 + b**2) #hypotenuse
print(c)

print(type(a),  type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)
print(pythagoras(3,4))