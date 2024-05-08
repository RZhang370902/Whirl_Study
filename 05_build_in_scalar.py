# Chapter 5-Built-in-Scalar-Types
# int x = 1
# float x = 1.0
# complex x = 1 + 2j
# bool x = True
# str x = 'abc'
# NoneType x = None

print("2^9 = ", 2**9)

x = 0.000005
y = 5e-6
print("0.000005 = 5e-6:", x == y)

x = 1400000.00
y = 1.4e6
print("1400000.00 = 1.4e6:", x == y)

print("float(1):", float(1))
print("Floating-point precision 0.1 + 0.2 == 0.3", 0.1 + 0.2 == 3)
print("float precision")
print("0.1 = {0:.17f}".format(0.1))
print("0.2 = {0:.17f}".format(0.2))
print("0.3 = {0:.17f}".format(0.3))
