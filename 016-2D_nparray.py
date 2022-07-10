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
#To get the number of lists and the number of elements in each list,
#or number of rows and columns, .shape:
arr_np.shape #(3, 3)
#To return the size of the array, .size:
arr_np.size #9
#To access to an item, [][] (a pair for dimension) or [,]:
arr_np[1][2] #30.0
arr_np[1,2] #30.0
#To slicing, [:,:] or [:][:]:
arr_np[1,1:3] #array([20., 30.])
arr_np[1:3,0] #array([10. , 11.1])
arr_np[1][1:3] #array([20., 30.])
arr_np[1:3][0] #array([10., 20., 30.])
#To add two arrays, +:
a=np.array([[0,1],[0,1]])
b=np.array([[10,11],[11,10]])
c=a+b
c #array([[10, 12],
  #       [11, 11]])
#To multiply by a scalar, *:
a2=2*a
a2 #array([[0, 2],
   #       [0, 2]])
#To multiply two arrays, or Hadamard product, *:
m=a*b
m #array([[ 0, 11],
  #       [ 0, 10]])
#To multiply two arrays with only equal number of columns in the first
#and number of rows in the second, np.dot(,):
x=np.array([[2,1],[2,1]])
y=np.array([[2,0,1,2],[2,1,1,0]])
z=np.dot(x,y)
z #array([[6, 1, 3, 4],
  #       [6, 1, 3, 4]])
#To calculate the sin, np.sin():
sin_z=np.sin(z)
sin_z #array([[-0.2794155 ,  0.84147098,  0.14112001, -0.7568025 ],
      #       [-0.2794155 ,  0.84147098,  0.14112001, -0.7568025 ]])
#To calculate the transposed matrix, .T:
z_t=z.T
z_t #array([[6, 6],
    #       [1, 1],
    #       [3, 3],
    #       [4, 4]])
