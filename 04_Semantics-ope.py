# Chapter 4

# addition, substration. multiplication
print((4 + 8) * (6.5 - 3))

#True division
print(11 / 2)

#Floor division
print(11 // 2)

#Bitwise operations
print(bin(10))

print(bin(9))

print(bin(9 | 10))

print(9 | 10)

#Assignment Operations
a = 24
print(a)
print(a + 2)
a += 2
print(a)

#Comparision Operations
# 25 is odd
print(25 % 2 == 1)

# 66 is odd
print(66 % 2 == 1)

# check if a is between 15 an 30
a = 25
print(15 < a < 30)

print(-1 == ~0)

print("---")
x = 4
print((x < 6) and (x > 2))
print((x > 10) or (x % 2 == 0))
print(not (x < 6))

# (x > 1) xor (x < 10)
print((x > 1) != (x < 10))

print("Indentity Operators")
#Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = [2, 3]

print(a == b)
print(a is b) # a and b is pointing to the same object
print(a is not b)

b = a
print(a is not b)
b = a + c
print(c in b)

c = 1
print("Membership operators")
print(1 in [1, 2, 3])
print(c in b)
