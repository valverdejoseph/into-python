#There are numpy arrays with more than one dimension (N-Dimensional)
import numpy as np
#2-Dimensional Arrays:
arr=[[0,1,2],[10,20,30],[11.1,12.2,13.3]]
arr_np=np.array(arr)
#A representation:
# [[ 0   , 1   ,  2],
#  [ 10  , 20  ,  30],
#  [ 11.1, 12.2, 13.3]]
#To obtain the number of dimensions, .ndim:
arr_np.ndim #2
#ndim as the number of nested lists
#To get the number of lists and the number of elements in each list, .shape:
arr_np.shape #(3, 3)
#To return the size of the array, .size:
arr_np.size #9


#indexing and slicing in 2d
#basic operations in 2d
