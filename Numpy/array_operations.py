import numpy as np


# -----------------SLICING--------------------
# [start:end], [start:end:step]

np0 = np.arange(10)
#print(np0)
#print(np0[1:3])         # [1 2]
#print(np0[:2])          # [0 1]
#print(np0[:])           # full array
#print(np0[::2])         # [0 2 4 6 8]

# Negative Slicing
np1 = np.arange(10)
#print(np1[-2:])          # [8 9]  
#print(np1[-6:-1:2])      # [4 6 8]

# Slicing Mult-Dim arrays
np2 = np.array([[[0,1,2],[2,3,4]],[[5,6,7],[8,9,9]],[[-1,-2,-3],[-4,-5,-6]],[[1,2,3],[1,1,1]]])       #3-dim array
#print(np2)                  
#print(np2[0:1, 0:1, 0:1])          # first elm of 1st array of 1st-dim
#print(np2[2, 0:1, 0:1])            # first elm of 1st array of 2nd-dim
#print(np2[0:3, 0:1, 0:2])           # first 2 elm of 1st array of EACH-dim 





#------------CHECKING DATA TYPE--------------
#--- if there is a string in the array, elm's types will be 'numpy.str'
various = np.array([[1,2,3],
                    [1,"Hello",3],
                    [4,5,5]])
#print(various.dtype)                # dtype = U21
#print(type(various[0][0]))          # element is '1' but its type is string 

st1 = np.array([1,2,3,4,5,6], dtype=np.int32)
st2 = np.array(['a','b','c'])
#print("st1's dtype is: ", st1.dtype, " and its class is ", type(st1[0]))  #int32, numpy.int32 (since fixed in definition)
#print("st2's dtype is: ", st2.dtype, " and its class is ", type(st2[0]))  #<U1, numpy.str

#--- if there is a non-default data type in the array, dtype = object
dictionary1 = {'1' : 'a'}
non_def = np.array([1,2,3,dictionary1])
#print(non_def.dtype)






#---------FILLING ARRAY WITHIN RANGE-------------
# np.linspace(start, end, howMany)
npLin = np.linspace(0,100,2)
#print(npLin)                        # [  0.  100.  ]

npLin1 = np.linspace(0,100,5)       # [  0.  25.  50.  75.  100.  ]
#print(npLin1)

npLin2 = np.linspace(0,100,101)     # [  0.  1.  2.  .........  100.  ]
#print(npLin2)


#-------------ARRAY METHODS---------------------

# APPEND = add to the end
a = np.array([1,2,3])
a = np.append(a, [7,8,9])

# INSERT = add to the index
a = np.insert(a, 3, [4,5,6])
#print(a)
arrToInsert = np.array([[1,1,1],
                        [2,2,2],
                        [4,4,4]])
#print(np.insert(arrToInsert, 2, [3,3,3], axis=0))
#print(np.insert(arrToInsert, 3, [0,0,0], axis=1))



# DELETE(array, indexNum) = delete the elm in the index no matter dim-number
arr = np.array([[1,2,3],
                [4,5,6],
                [6,7,8]])
#print(np.delete(arr, 3))     #deleted '4'
#print(np.delete(arr, 0, axis=0))   # deleted the row(axis=0, horizontal) with index '0'
#print(np.delete(arr, 1, axis=1))   # deleted the column(axis=1, vertical) with index '1'


#------------STRUCTURING METHODS-----------------

# SHAPE/RESHAPE
ar = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

#print(ar.shape, "\n")
#print(ar.reshape((2,8)), "\n")     #when shaping, reshape() conserves the elm count
#print(ar.reshape((16,)), "\n")
#print(ar.reshape((4,2,2)), "\n")   
#print(ar.reshape((16,1)))


# RESIZE
ar.reshape((16,1))
#print(ar)               
# 'ar' array will not change, "reshape" method works on a copy. However;
ar.resize((16,1))
#print(ar)
# Now 'ar' array has been modified permanently!


# FLATTEN - RAVEL - .FLAT
ar.resize((4,4))
# take a copy of the array and flatten it
var1 = ar.flatten()
var1[2] = 100
#print(var1)    # index 2 has the value of '100' but,
#print(ar)      # the actual array 'ar' haven't changed


# take the array itself and ravel it 
var2 = ar.ravel()
var2[4] = 99
#print(var2)     # index 4 has the value '99'
#print(ar)       # also the original array's index 4 has the value '99'


var = [v for v in ar.flat]    # '.flat' attribute states the flattened array
print(ar.flat)                # 'ar.flat' cannot be printed
print(var)              
# output >> [1, 2, 3, 4, 99, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]



# TRANSPOSE - T - SWAPAXES
arr.resize((4,4))

#print(ar.swapaxes(0,1)) # '0' stands for axis=0, '1' stands for axis=1, That means Rows and Columns are swapped
#print(ar.T)             # same thing with swapaxes(0,1), matrix is transposed
#print(ar.transpose())   # another way to 'transpose'

#all outputs will be same which is the transposed 'arr'
