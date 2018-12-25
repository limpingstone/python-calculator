from operand import *
from function import *

n1 = Number(1)
n2 = Number(2)
n3 = Number(3)

x = Variable()
y = Variable()
#!/usr/bin/env python3
#
# run_test.py - By Steven Chen Hao Nyeo 
# Test script for the calculator backend
# Last Modified: December 24, 2018

b1 = BinaryOp(x, '+', n3)
b2 = BinaryOp(x, '-', n3)
b3 = BinaryOp(x, '*', n3)
b4 = BinaryOp(x, '/', n3)

b = BinaryOp(x, '+', n1)


# BinaryOp test
print("--------------------------------\nBinaryOp Test")
print("5 + 3 = " + str(b1.get_value(5)))
print("5 - 3 = " + str(b2.get_value(5)))
print("5 * 3 = " + str(b3.get_value(5)))
print("5 / 3 = " + str(b4.get_value(5)))

print(str(b1.derivative()))
print(str(b2.derivative()))
print(str(b3.derivative()))
print(str(b4.derivative()))

print(b1.derivative().get_value(5)) # (x + 3)' = 1
print(b2.derivative().get_value(5)) # (x - 3)' = 1
print(b3.derivative().get_value(5)) # (x * 3)' = 3
print(b4.derivative().get_value(5)) # (x + 3)' = 1/3

print(b1.derivative().equals(b.derivative()))


# Polynomial Test
print("--------------------------------\nPolynomial Test")
poly1 = Polynomial(Variable(), 2)
poly2 = Polynomial(poly1, 3)
print(poly1)
print(poly1.get_value(4))
print(poly2)
print(poly2.derivative())
print(poly2.derivative().get_value(1))

print(poly1.derivative().equals(poly2.derivative()))

# Function tests
print("--------------------------------\nSine")
sinx2 = Sin(poly1)
print(sinx2)
print(sinx2.derivative())
print(Sin(Variable()).get_value(math.pi / 2))
print(Sin(Variable()).derivative().get_value(math.pi / 2))

print("--------------------------------\nCosine")
cosx2 = Cos(poly1)
print(cosx2)
print(cosx2.derivative())
print(Cos(Variable()).get_value(math.pi / 2))
print(Cos(Variable()).derivative().get_value(math.pi / 2))

print("--------------------------------\nExponential")
exp = Exp(poly1)
print(exp)
print(exp.derivative())
print(Exp(Variable()).get_value(math.pi)) # e ^ pi = 23.14
