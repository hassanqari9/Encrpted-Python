# Random Permutations
# Random permutation is a random reordering of the elements in an array.
# Use the shuffle() method to shuffle the elements of an array.

# e.g [4,5,6] -> [6,4,5]

from numpy import random
import numpy as np

# Shuffle the elements of the array
a = np.array([1, 2, 3, 4, 5])
random.shuffle(a) # modifies the original array
print(a)

# use permutation() to create a permutation of an array
b = np.array([1, 2, 3, 4, 5])
Happy = random.permutation(b) # does not modify the original array
print(b)
print(Happy)

s = random.shuffle(b)
print(s) # None because shuffle() modifies the original array