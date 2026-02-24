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

def pythagoras(a, b): return math.sqrt(a**2 + b**2)
print(pythagoras(3,4))
print("Function practice:")
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def traingle_area(w, h): return rectangle_area(w, h) / 2
def celsius_to_fahrenheit(d): return d * (9/5) + 32
print(celsius_to_fahrenheit(35))
def mph_to_kph(s): return s * 1.609
print(mph_to_kph(10))
def arith_mean(x, y, z): return (x + y + z) / 3
print(arith_mean(3, 3, 3))