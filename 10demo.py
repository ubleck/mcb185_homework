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

c = 2
d = 2
if c == d:
    print('c equals d')
print(c, d)

def is_even(x):
    if x % 2 == 0: return True
    return False
print(is_even(2))
print(is_even(3))

e = c == d
print(e)
print(type(e))

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you aer living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
print(abs(a-b)) #5.551115123125783e-17
if abs(a-b) < 1e-9: print('close enough')
if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')
 
print('Hi')

x = 10
def is_integer(x):
    if x % 2 == 0: print('is integer')
    else:          print('not integer')

is_integer(x)

print(x)

g = 1.000000000001
def is_validp(g):
    if g <= 1: print(g, 'is valid probability')
    else:      print(g, ' is not a valid probability')
is_validp(g)

w = 'U'
def dnaweight(w):
    if   w == 'A': print('331.22g/mol')
    elif w == 'C': print('307.19g/mol')
    elif w == 'G': print('347.22g/mol')
    elif w == 'T': print('322.21g/mol')
    else: print('None')
dnaweight(w)

c = 'U'
def dnacomp(c):
    if   c == 'A': print('T')
    elif c == 'C': print('G')
    elif c == 'G': print('C')
    elif c == 'T': print('A')
    else:          print('None')
dnacomp(c)    