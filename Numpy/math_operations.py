import numpy as np


"np.nan stands for 'Not A Number'"
"np.inf stands for 'Infinite'"

# checking real number with 'np.isnan()'
np1 = np.sqrt(-25)
#print(np1)                  # >> nan = NOT A NUM
#print(np.isnan(np1))        # >> True 


# checking infinity with 'np.isinf()'
np2 = np.array([10]) / 0     # divide the list's elms to 0 to get infinity
#print(np2)                  # >> [inf]
#print(np.isinf(np2))        # >> [ True ]


#-------------MATHEMATICAL OPERATIONS--------------
"In numpy (unlike python), arrays can be manipulated by math ops"

s1 = np.array([1,2,3])
s2 = np.array([4,5,6])
#print(s1 + s2)          # >> [5 7 9]    (vector addition)


a1 = np.array([1,2,3]) 
a2 = np.array([[1],
               [2]])
#print(a1*a2)            # >> [[1 2 3] [2 4 6]]  (matrix mult.)


op = np.array([[1,2,3],
               [4,5,6]])
#print(np.sqrt(op))              #
#print(np.cos(op))               # element-wise mathematical operations
#print(np.arctan(op))            # FOR MORE: https://numpy.org/doc/stable/reference/routines.math.html
#print(np.log10(op))             #
#print(np.exp(op))


