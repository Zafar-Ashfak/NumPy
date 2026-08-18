import numpy as np
import matplotlib.pyplot as plt

arr1 = np.arange(5, 51, 5)

arr2 = np.array([3, 9, 1, 4, 5, 2, 8, 3, 2])

arr3 = np.array([[1, 5, 9, 2],
                 [6, 3, 1, 7],
                 [5, 2, 9, 1],
                 [7, 4, 8, 3]])


# Saving arrays as file
np.save('myarr1.npy', arr1)
np.save('myarr2.npy', arr2)
np.save('myarr3.npy', arr3)

# Loading files as array
my_arr1 = np.load('myarr1.npy')
print(my_arr1)

my_arr2 = np.load('myarr2.npy')
print(my_arr2)

my_arr3 = np.load('myarr3.npy')
print(my_arr3)
