import numpy as np

# Array Creation

# 1. array() method can take list or tuple
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

arr2 = np.array((11, 22, 33, 44, 55))
print(f"\n{arr2}")

# 2. arange() creates an array using start, stop, and step
arr3 = np.arange(1, 11) # 11 is not inclusive
print(f"\n{arr3}")

arr4 = np.arange(2, 21, 2)
print(f"\n{arr4}")

py_list = [1, 2, 3]
np_arr = np.array([1, 2, 3])

print(f"Python list: {py_list * 2}") # prints list twice
print(f"Numpy array: {np_arr * 2}") # prints each element with multiply by 2

zeros =  np.zeros((4, 3))
print(f"\n{zeros}")

ones = np.ones((3, 5))
print(f"\n{ones}")

full = np.full((4, 4), 99)
print(f"\n{full}")

random = np.random.random((3, 4))
print(f"\n{random}")

# print even numbers
even_nums = np.arange(2, 31, 2)
print(f"\nEven numbers: {even_nums}")

# print odd numbers
odd_nums = np.arange(1, 32, 2)
print(f"\nOdd numbers: {odd_nums}")

# Vector or 1D Array
vector = np.arange(1, 21)
print(f"\nVector: {vector}")

# Matrix or 2D Array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"\nMatrix: {matrix}")

# Tensor or 3D+ Array
tensor = np.array([
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
            ],
            [
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ],
])

print(f"Tensor: {tensor}")