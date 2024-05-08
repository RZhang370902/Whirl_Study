# Chapter 3-Semantics-Variables

x = 1           # x is an integer
x = 'hello'     # now x is a string
x = [1 ,2 ,3]   # now x is a list

y = x
print(y)

x.append(4) #append 4 to the list pointed to by x
print(y) #y's list is modified here .append(4) directly changes the object y is poing to

x = 'something else'
print("hi", y)

y = x
print("oh", y)

x = 10
y = x
x += 5 # add 5 to x's value, and assign it to x
print("x =", x)
print("y =", y)

x = 4
print(type(x))

x = 'hello'
print(type(x))

x = 3.14159
print(type(x))

L = [1, 2, 3]
L.append(100)
print(L)

x = 4.5
print(x.real, "+", x.imag, "i")

x =4.5
print(x.is_integer())
      
x = 4.0
print(x.is_integer())

print(type(x.is_integer))

