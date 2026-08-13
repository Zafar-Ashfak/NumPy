import numpy as np
import time

# ************************* Array Creation *************************
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

# ************************* Python List Vs NumPy Array *************************
py_list = [1, 2, 3]
np_arr = np.array([1, 2, 3])

print(f"\nPython list + list: {py_list + py_list}")
print(f"NumPy array + array: {np_arr + np_arr}")

print(f"Python list x list: {py_list * 2}") # prints list twice
print(f"Numpy array x list: {np_arr * 2}") # prints each element with multiply by 2

# ************************* Checking list and array execution time *************************

start = time.perf_counter()
my_list = [i * 2 for i in range(1_000_000)]
list_time = time.perf_counter() - start

start = time.perf_counter()
my_arr = np.arange(1_000_000) * 2
numpy_time = time.perf_counter() - start

print(f"Python list execution time: {list_time:.6f} seconds")
print(f"NumPy array execution time: {numpy_time:.6f} seconds")

# ************************* All zeros matrix *************************
zeros =  np.zeros((4, 3))
print(f"\n{zeros}")

# ************************* All ones matrix *************************
ones = np.ones((3, 5))
print(f"\n{ones}")

# ************************* full matrix with all 99 elements *************************
full = np.full((4, 4), 99)
print(f"\n{full}")

# ************************* All random elements matrix *************************
random = np.random.random((3, 4))
print(f"\n{random}")

# ******************** Some addition Operations *******************
# print even numbers
even_nums = np.arange(2, 31, 2)
print(f"\nEven numbers: {even_nums}")

# print odd numbers
odd_nums = np.arange(1, 32, 2)
print(f"\nOdd numbers: {odd_nums}")


# ****************** Vector, Matrix and Tensor **********************

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


# ************************* Array's Properties *************************
np_arr = np.array([[1, 7, 3, 9],
                   [5, 2, 1, 6],
                   [4, 8, 3, 5]])

print(f"\nArray's Shape: {np_arr.shape}")
print(f"Size of the array: {np_arr.size}")
print(f"Array dimension: {np_arr.ndim}D")
print(f"Array's data type: {np_arr.dtype}")
print(f"Each element of the array consuming : {np_arr.itemsize} bytes")
print(f"Total memory consuming by array is: {np_arr.nbytes} bytes")
print(f"Flags: {np_arr.flags}")

print(f"\nOriginal Matrix: {np_arr}")
print(f"Transposed Matrix:{np_arr.T}")

# ******************* Slicing and Sorting on Vector *******************
print("\nSlicing operation on vector")
vec = np.array([2, 9, 6, 5, 1, 8, 4, 3, 7, 6, 1, 9])
print(vec[1: 6])
print(vec[ : 9])
print(vec[5 : ])
print(vec[0 : 10: 2])
print(vec[::-1])

print("\nSorting operation on vector")
sorted_vec = np.sort(vec)
print(sorted_vec)

# ******************* Slicing and Sorting on Matrix *******************
print("\nSlicing operation on matrix")
matrix = np.array([[2, 1, 5, 8],
                   [6, 3, 2, 4],
                   [5, 7, 9, 2],
                   [1, 5, 6, 3]])


print(f"Specific element: {matrix[0, 3]}") # 8
print(f"Specific element: {matrix[2, 1]}") # 7
print(f"Specific element: {matrix[1, 2]}") # 2

print(matrix[1]) # prints entire row
print(matrix[:, 2]) # prints entire col

print("\nSorting operation on matrix")
print(f"Row wise sorting: {np.sort(matrix, axis=1)}")
print(f"\nColumn wise sorting: {np.sort(matrix, axis=0)}")

# ******************* Filtering *******************
arr = np.array([12, 7, 19, 13, 5, 8, 3, 16, 2, 8, 7, 9, 1, 5, 11, 4, 16, 19, 14])
print("Array greater than 25:", arr[arr > 15])

mask = arr % 2 == 0
print(f"Even nums: {arr[mask]}")

# ******************* Indices *******************
indices = [1, 2, 6, 8, 9] # 7 19 3 2 8
print(f"Elements at indices: \n{indices}\n{arr[indices]}")

# ******************* where(condition) method *******************
odds = np.where(arr % 2 != 0)
print(f"\nOdd elements in the array are: {arr[odds]}")

# ******************* where(condition, x, y) method *******************



