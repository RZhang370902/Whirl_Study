# Chapter 3-Semantics-Variables

x = 1           # x is an integer
x = 'hello'     # now x is a string
x = [1 ,2 ,3]   # now x is a list

y = x
print(y)

x.append(4) #append 4 to the list pointed to by x
print(y) #y's list is modified here .append(4) directly changes the object y is poing to

x = 'something else'
print('hi', y)

y = x
print('oh', y)
