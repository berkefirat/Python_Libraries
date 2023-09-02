import numpy as np

#--------SAVE AS .npy FILE
a1 = np.array([[1,2,3,4,5],[6,7,8,9,0],[9,9,9,9,9]])
#np.save("myArray.npy", a1)    #saves the array as a .npy file named 'myArray'

loadedArr1 = np.load("myArray.npy")
#print(loadedArr)



#--------SAVE AS .csv FILE
a2 = np.array([[1,2,3,4,5],[6,7,8,9,0],[9,9,9,9,9]])
#np.savetxt("myArray.csv", a2, delimiter=",")

loadedArr2 = np.loadtxt("myArray.csv", delimiter=",")
#print(loadedArr2)




