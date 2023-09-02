# Covered features: 
# np.array, .shape, np.arange, np.zeros, np.full, .ndim


import numpy as np

# ndarray = n-dimensional arrays

np1 = np.array([0,1,2,3,4,5])
#print(np1)

#print(np1.shape)  # (6,)


# Range 
np2 = np.arange(6)
#print(np2)          # [0 1 2 3 4 5]


# Step
np3 = np.arange(0,10,2)
#print(np3)          # [0 2 4 6 8]

# Zeros
np4 = np.zeros(10)
#print(np4)             # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Ones
npOnes = np.ones((2,2))
#print(npOnes)

# Empty - fills the described array with random values and allocates memory
npEmpty = np.empty((2,2,2))
#print(npEmpty)


# Multidimensional Zeros
np5 = np.zeros((4,10))      # np.zeros((row, column))
#print(np5)                  # 4-dimensional, 10 element 0 lists

# Full
np6 = np.full((10),6)      # np.full((size), digit)
#print(np6)                 # [6 6 6 6 6 6 6 6 6 6]


# Multidimensional Full
np7 = np.full((2,10),6)    # np.full((row,column), digit)
#print(np7)


# Converting python list to numpy array
myList = [1,2,3,4,5]
np8 = np.full((6,5),myList)   # np.full((row,colSize) myList)  |  colSize = sizeOfmyList
#print(np8[0,0])                 # np[0] = [1 2 3 4 5] --- np[0,0] = 1


# Not only integers, chars, bools etc...
np9 = np.full((10),"hey")
np0 = np.full((2,2,2,2),'i')     # np.full(1-dim, 2-dim, 3-dim, 4-dim, ....)
#print(np9)
#print(np0)


# Ones
npOnes = np.ones((2,2))
#print(npOnes)


# Empty - fills the described array with random values and allocates memory
npEmpty = np.empty((2,2,2))
#print(npEmpty)


# Checking Number of the Dimension
ex1 = np.array(42)                                          # 0-dim
ex2 = np.array([1,2,3,4,5])                                 # 1-dim
ex3 = np.array([[1,2,3],[4,5,6]])                           # 2-dim
ex4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[-1,-2,-3]]])    # 3-dim
#                                                           # n-dim ...
#print(ex1.ndim)
#print(ex2.ndim)
#print(ex3.ndim)
#print(ex4.ndim)


# Setting Dimension = .ndmin
arr = np.array([1,2,3,4,5], ndmin=4)  
#print(arr)                  # [[[[1 2 3 4 5]]]]
#print(arr.ndim)             # 4-dim         


