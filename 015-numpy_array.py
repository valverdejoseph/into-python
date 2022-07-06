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
#To change an item, []=:
arreal[2]=100
arreal #array([  3.14, 500.  , 100.  ,   4.  ])
#To slicing, [:]:
arreal[1:3] #array([500., 100.])
#For multiple assignment, [:]=:
arreal[2:4]=3.4,10
arreal #array([  3.14, 500.  ,   3.4 ,  10.  ])

#Basic operations are usually faster and require less memory
#with Numpy compared to regular Python
#Vector addition with Numpy:
x=np.array([1,0])
y=np.array([0,1])
z=x+y
z #array([1, 1])
#Vector addition with regular Python:
x=[1,0]
y=[0,1]
z=x+y # XXXXX
z #[1, 0, 0, 1] XXXXX
z=[]
for i,j in zip(x,y):
  z.append(i+j)
z #[1, 1]
#Vector subtraction is similar
#Vector multiplication with a scalar with Numpy:
x=np.array([0.2,5])
z=2*x
z #array([ 0.4, 10. ])
#Vector multiplication with a scalar with regular Python:
z=[]
for i in x:
  z.append(2*i)
z #[0.4, 10.0]
#Hadamard product: Product of two numpy arrays:
#With Numpy:
w=[4,2]
z=x*w
z #array([ 0.8, 10. ])
#With regular Python:
x=[0.2,5]
z=[]
for i,j in zip(x,w):
  z.append(i*j)
z #[0.8, 10]
#Dot product:
x=np.array([3.2,4])
z=np.dot(x,w)
z #20.8
#Adding constant to an array with Broadcasting property:
#Broadcasting: effect affects each item
z=x+8
z #array([11.2, 12. ])

#Universal functions: They operate on N-dimensional arrays
arr0=np.array([1,2,2,1,-1])
#To return the mean or average value, .mean():
mean_0=arr0.mean()
mean_0 #1.0
#To return the maximum value, .max():
max_0=arr0.max()
max_0 #2
#To return the value of Pi, np.pi:
the_pi=np.pi
the_pi #3.141592653589793
#To return the function sin(x) with x in radians, .sin():
sin_0=np.sin(arr0)
sin_0 #array([ 0.84147098,  0.90929743,  0.90929743,  0.84147098, -0.84147098])
#To return spaced numbers over an interval, .linspace():
arr1=np.linspace(-10,10,num=8)
arr1 #array([-10.        ,  -7.14285714,  -4.28571429,  -1.42857143,   1.42857143,   4.28571429,   7.14285714,  10.        ])
#Another example:
x=np.linspace(0,2*np.pi,5)
y=np.sin(x)
import matplotlib.pyplot as plt #to plot the function
#To install, in terminal: pip install matplotlib
plt.plot(x,y)
plt.show() #This opens in a window
#If you are in a jupyter notebook, try with:
%matplotlib inline #and plt.plot(x,y)
