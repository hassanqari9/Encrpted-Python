# Numpy Properties

# x.reshape(2, 3) - will reshape the array to 2 rows and 3 columns
# x.size - will return the number of elements in the array
# x.shape - will return the shape of the array
# x.dtype - will return the data type of the elements in the array
# x.itemsize - will return the size of the elements in the array in bytes




import numpy as np

ar = np.array([[1, 2, 3], [4, 5, 6], [7, 1, 0]])

print(ar.reshape(3, 3)) # [[1 2 3 4 5 6 7 1 0]]

print(ar.size) # 9

print(ar.shape) # (3, 3)