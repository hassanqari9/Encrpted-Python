# reduce - takes two values from the list and applies the function to them

# e.g list = [1, 2, 3, 4, 5]
# and the function is add
# reduce would do the following:
# add(1, 2) = 3
# add(3, 3) = 6
# add(6, 4) = 10
# add(10, 5) = 15

# incase a function is something like increases the variables, then reduce would get stuck in infinite loop

from functools import reduce
L = [1, 2, 3, 4, 5]
s = reduce(lambda x, y: x+y, L)
print(s)