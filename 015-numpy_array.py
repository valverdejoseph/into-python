#Numpy is a library for scientific computing, and also the basis for Pandas
import numpy as np
#To create a one-dimensional Numpy array, np.array([]):
arr=np.array([1,3,5,7,9])
#each item is of the same type
arr #array([1, 3, 5, 7, 9])
type(arr) #<class 'numpy.ndarray'>
#To access an item, []:
arr[0] #1
arr[2] #5
#To check the data type:
arr.dtype #dtype('int64')
type(arr[2]) #<class 'numpy.int64'>
#To get the number of elements, .size:
arr.size #5
#To get the number of array dimensions, .ndim:
arr.ndim #1
#To get a tuple of the sizes of the array in each dimension, .shape:
arr.shape #(5,)
#Another example with floats:
arreal=np.array([3.14,500,23.5,4])
type(arreal) #<class 'numpy.ndarray'>
arreal.dtype #dtype('float64')

#Indexing and slicing
#Basic operations
#Universal functions
#a
