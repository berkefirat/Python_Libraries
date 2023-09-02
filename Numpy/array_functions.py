import numpy as np


#---------APPEND--DELETE----------

# 'np.append(array, [arrToAppend])'
a = np.array([1,2,3])
a = np.append(a, [4,5,6])
#print(a)


# 'np.delete(array, ElmIndex)'
b = np.array([1,2,3])
b = np.delete(b, 1)         #delete the elm with index 1
#print(b)

c = np.array([[1,2,3],
              [4,5,6]])
#print(np.delete(c, 0))
#print(np.delete(c, 2))
#print(np.delete(c, 5))

#print(np.delete(c, 1, 0))   # 3rd parameter '0' means DELETE THE ROW >> [[1 2 3]]
#print(np.delete(c, 1, 1))   # 3rd parameter '1' means DELETE THE COLMN >> [[2 3]
#                                                                          [5 6]]





#--------INTEGRATE or SPLIT ARRAYS---------
a1 = np.array([[1,2,3,4,5],
               [6,7,8,9,10]])
a2 = np.array([[11,12,13,14,15],
                [16,17,18,19,20]])

# CONCATENATE
c1 = np.concatenate((a1,a2), axis=0)    # axis=0 means arrays will be concatenated vertically

c2 = np.concatenate((a2,a1), axis=1)    # 'a2' is on top, axis=1 means arrays will be concatenated horizontally

#print(c1, '\n') 
#print(c2)



# STACK
st = np.stack((a1,a2))      # when stacking, adds another dimension. 
#print(st)                   # Stacking two seperate 2-dim array will result in 3-DIM array

stEX1 = np.array([[[1,1,1],[2,2,2]],
                  [[3,3,3],[4,4,4]]])
stEX2 = np.array([[[0,0,0],[0,0,0]],
                  [[0,0,0],[0,0,0]]])
stNew = np.stack((stEX1, stEX2))    # stacking two 3-dim array will result in 4-dim array
#print(stNew)

st2 = np.vstack((a1,a2))            
st3 = np.hstack((a1,a2)) # WHEN USING H/VSTACK, IT DOES CONCATENATING. DOES NOT INCREASE THE DIMENSION
#print(st2, '\n')
#print(st3)



# SPLIT
sp = np.array([[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])

#print(np.split(sp, 2, axis=0))     #split the array horizontally. Means dividing into Rows by twos
#print(np.split(sp, 3, axis=1))     #split the array vertically. Means dividing into Columns by twos
# the shape of the array must be divisible to desired portion





#!!!----------AGGREGATE-FUNCTIONS----------!!!
nA = np.array([[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])


#print(nA.min())         # min value
#print(nA.max())         # max value
#print(nA.mean())        # mean value of the array
#print(nA.std())         # standard deviation of the elms
#print(nA.sum())         # sum of the elms
#print(np.median(nA))    #median value of the array


#---------RANDOMNESS of NUMPY------------

# random RANDINT
number = np.random.randint(100)     # a random integer betw '0-100'
#print(number)

numbers = np.random.randint(90, 100, size=(2,3,4))  
#print(numbers)                       # array of rand integers betw '90-100' with shape(2,3,4)


# random BINOMIAL
bin = np.random.binomial(10, p=0.5, size=(10,))   
#print(bin)                            # 10 tries, probability=0.5, flipCoin=10 times 


# random NORMAL
norm = np.random.normal(loc=170, scale=15, size=(2,8))
#print(norm)         # array of rand integers with in between 170+/-15


# random CHOICE
a = np.random.choice([10,20,30,40,50,60], size=(5,10))
#print(a)        #array of randomly chosen numbers from determined array with size=(5,10)
