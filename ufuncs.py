import numpy as np
from math import log


# Add the elements of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(list3)
print()

# same as above, but using zip
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [x + y for x, y in zip(list1, list2)]
print(list3)
print()

# same as above, but using add function
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = np.add(list1, list2)
print(list3)
print()

# create your own ufunc for addition


def myadd(x, y):
    return x + y


myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print()

# check if a function is a ufunc
print(type(np.add))
print(type(myadd))
print(np.concatenate)
print()

# use an if statement to check if the function is a ufunc or not
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')
print()

# subtract the values of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
newlist = np.subtract(list1, list2)
print(newlist)
print()

# multiply the values of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
newlist = np.multiply(list1, list2)
print(newlist)
print()

# divide the values of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
newlist = np.divide(list1, list2)
print(newlist)
print()

# power the values of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
newlist = np.power(list1, list2)
print(newlist)
print()

# find the remainder of the values of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
newlist = np.mod(list1, list2)
print(newlist)
print()

# return the quotient and mod of two lists using divmod()
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
quotient, remainder = np.divmod(list1, list2)
print(quotient)
print(remainder)
print()

# absolute values of a list
list1 = [-1, -2, 1, 2, 3, -4]
newlist = np.absolute(list1)
print(newlist)
print()

# round off the values of a list
list1 = [1.1, 1.5, 1.9, 2.1, 2.5, 2.9]
newlist = np.around(list1)
print(newlist)
print()

# round off the values of a list using truncate
list1 = [1.1, 1.5, 1.9, 2.1, 2.5, 2.9]
newlist = np.trunc(list1)
print(newlist)
print()

# round off the values of a list using fix
list1 = [1.1, 1.5, 1.9, 2.1, 2.5, 2.9]
newlist = np.fix(list1)
print(newlist)
print()

# floor of the values of a list
list1 = [1.1, 1.5, 1.9, 2.1, 2.5, 2.9]
newlist = np.floor(list1)
print(newlist)
print()

# ceil of the values of a list
list1 = [1.1, 1.5, 1.9, 2.1, 2.5, 2.9]
newlist = np.ceil(list1)
print(newlist)
print()

# log at base 2 of the values of a list
list1 = np.arange(1, 10)
newlist = np.log2(list1)
print(newlist)
print()

# log at base 10 of the values of a list
list1 = np.arange(1, 10)
newlist = np.log10(list1)
print(newlist)
print()

# log at base e of the values of a list
list1 = np.arange(1, 10)
newlist = np.log(list1)
print(newlist)
print()

# log at any base of the values of a list
list1 = np.arange(1, 10)
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
print()

# sum the values in arr1 and arr2
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
newarr = np.sum([arr1, arr2])
print(newarr)
print()

# sum the values in arr1 and arr2 over axis 1
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
print()

# cummulative sum of the values in an array
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)
print()

# product of the values in an array
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)
print()

# product of the values in arr1 and arr2
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2])
print(newarr)
print()

# product of the values in arr1 and arr2 over axis 1
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
print()

# cummulative product of the values in an array
arr = np.array([1, 2, 3, 4])
newarr = np.cumprod(arr)
print(newarr)
print()

# find the difference between adjacent values in an array
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
print()

# find the difference between adjacent values in an array twice
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
print()

# find the LCM (Least Common Multiple) of two numbers
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
print()


# find the LCM of all of the numbers in an array
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
print()

# find the GCD (Greatest Common Denominator) of two numbers
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
print()

# find the GCD of all of the numbers in an array
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
print()

# find the sine of pi/2
x = np.sin(np.pi / 2)
print(x)

# find the sine of each element in arr
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.sin(arr)
print(x)
print()

# find the angle of each element in arr, in radians
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
print()

# convert all of the values in arr from radians to degrees
arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
x = np.rad2deg(arr)
print(x)
print()

# find the angle of 1.0
x = np.arcsin(1.0)
print(x)
print()

# find the angle for all of the tanh values in arr
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
print()

# find the angle for all of the sine values in arr
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)
print()

# find the hypotenuse for 4 and 3
base = 4
perp = 3
x = np.hypot(base, perp)
print(x)
print()

# find the sinh of pi/2
x = np.sinh(np.pi / 2)
print(x)
print()

# find the sinh value for all of the elements in arr
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.sinh(arr)
print(x)
print()

# find the cosh of pi/2
x = np.cosh(np.pi / 2)
print(x)
print()

# find the cosh value for all of the elements in arr
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.cosh(arr)
print(x)
print()

# convert an array with repeating elements to a set
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.unique(arr)
print(x)
print()

# find the union of two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
print()

# find the intersection of two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
print()

# find the difference between two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr)
print()

# find the elements that are not present in both arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr)
print()
