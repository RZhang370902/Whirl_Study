# set the midpoint
# comments are marked by#
midpoint = 5

# make two empty lists
lower = []; upper = []

# split the numbers into lower and upper
for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)

print("lower:", lower)
print("upper:", upper)

# x += 2 is shorthand for x = x + 2

x = 0

for i in range(5):
    x += 2
    print(x)


L = [4,2,3,1]
L.sort()
print(L)
