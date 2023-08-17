import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(np.__version__)
print()

arr = np.array(42)
print(arr)
print()

# 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print()

# 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print()

# Check Number of Dimensions
print(arr.ndim)
print()

# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
print()

# Access Array Elements
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3])
print()

# Access 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st dim: ', arr[0, 1])
print('5th element on 2nd dim: ', arr[1, 4])
print()

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [
                10, 11, 12]]])
print(arr[0, 1, 2])
print()

# Negative Indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim: ', arr[1, -1])
print()

# Slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[::2])
print()

# Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])
print()

arr = np.array([10, 15, 20, 25, 30, 35, 40])
# everything from (including) the second item to (not including) the fifth item
print(arr[1:4])
print()

# Data Types in Python
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
print()

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
print()

# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
print()

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
print()

# Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print()

# change data type from float to integer by using 'i' as parameter value
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
print()

# change data type from integer to boolean
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
print()

# make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
print()

# make a view, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
print()

# make a view, change the view, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)
print()

# Check if Array Owns it's Data
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
print()

# Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
print()

# create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
print()

# Reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 4)
print(newarr)
print()

# Reshape From 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, 2)
print(newarr)
print()

# Check if the returned array is a copy or a view:
print(arr.reshape(2, 4).base)
print()

# unknown dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
print()

# Flattening the arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
print()

# Iterating Arrays
arr = np.array([1, 2, 3])
for x in arr:
    print(x)
print()

# Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)
print()

# iterate on each scalar element of the 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)
print()

# Iterating 3-D Arrays
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in arr:
    print(x)
print()

# iterate down to the scalars
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
print()

# Iterating Arrays Using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
print()

# Iterating Array With Different Data Types
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
print()

# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)
print()

# Enumerated Iteration Using ndenumerate()
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print()

# Enumerated Iteration Using ndenumerate()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print()

# Joining NumPy Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
print()

# Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print()

# Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print()

# Stacking Along Rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)
print()

# Stacking Along Columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)
print()

# Stacking Along Height (depth)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)
print()

# Splitting NumPy Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print()

# split into arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
print()

# split 2-D array into three 2-D arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
newarr = np.array_split(arr, 3)
print(newarr)
print()

# split 2-D array into three 2-D arrays along rows
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
print()

# use the hsplit() method to split the 2-D array into three 2-D arrays along rows
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = np.hsplit(arr, 3)
print(newarr)
print()

# search an array for a certain value, and return the indexes that get a match
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
print()

# find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)
print()

# sort an array  in order numerically
arr = np.array([4, 3, 8, 1, 2, 6, 7, 5])
print(np.sort(arr))
print()

# sort an array alphabetically
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
print()

# sort a boolean array
arr = np.array([True, False, True])
print(np.sort(arr))
print()

# sort a 2-D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
print()

# search sorted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
print()

# search from the right side
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
print()

# search for multiple values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
print()

# filter out all odd numbers from an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = [i for i in arr if i % 2 == 0]
print(x)

# filter using a boolean index list
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
print()

# create a filter array that will return only values higher than 42
arr = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print()
