from functools import reduce

f = open("try.txt", "r")
t = f.read()
print(t)
f.close()

###

f = open("try.txt", "w")
t = f.read()  # will give error
t = f.write("Welcome")
print(t)
f.close()

###

# will close the file automatically
with open("try.txt", "r") as f:
    t = f.read()
    print(t)

# line by line read
f = open("try.txt", "r")
while True:
    t = f.readline()
    print(t)
    if not t:
        break
f.close()

# split

# split("#", 2)
# 2 is the maxsplit

f = open("try.txt", "r")
t = f.read()
print(t.split("#", 2))
f.close()

###
f = open("try.txt", "r")
i = 0
while True:
    i = i + 1
    t = f.readline()
    if not t:
        break
    L1 = t.split(",")[0]
    L2 = t.split(",")[1]
    L3 = t.split(",")[2]
    print(f" First value of line {i} is {L1}")
    print(f" Second value of line {i} is {L2}")
    print(f" Third value of line {i} is {L3}")

    type(L1)  # str
    # before using L1, L2, L3, convert them to int or float or appropriate type
    # L1*12 will give L1 12 times, not the multiplication: 12 * 12
    # int(L1)*12 will give the multiplication
    f.close()

###
# welcome to IUST
# seek and tell
# seek will move the cursor to the given position
# tell will tell the current position of the cursor
with open("try.txt", "r") as f:
    f.seek(8)
    t = f.read()
    print(t)
    print(f.tell())

# member functions


def square(x):
    return x*x


print(square(3))

L = [3, 4, 5, 7, 3, 8]
L1 = []

for i in L:
    L1.append(square(i))

# same thing can be done using map
L = [3, 4, 5, 7, 3, 8]
# why not square(L) ? because map will apply the function to each element of L
L1 = list(map(square, L))
# higher order function - function that takes another function as argument

# filter
L = [3, 4, 5, 7, 3, 8]


def filter_fn(x):
    return x > 4


L2 = list(filter(filter_fn, L))

# lambda function
L3 = list(map(lambda x: x*x, L))

# reduce
L = [1, 2, 3, 4, 5]
s = reduce(lambda x, y: x+y, L)
print(s)

# lembda is same as
def add(x, y):
    return x+y
s = reduce(add, L)