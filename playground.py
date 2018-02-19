import site
import numpy as np
import math

# site packages
print(site.getsitepackages())

# array -> dictionary
A = ['one', 'two', 'three']
hashmap = dict(np.ndenumerate(A))

# inserting row into matrix
a = np.array([[1, 1], [2, 2], [3, 3]])
print(a)

bias = np.ones((a.shape[0], 1), dtype=int)
print(bias)

b = np.concatenate((bias, a), axis=1)
print(b)

# random number initialization for matrix
A = np.random.uniform(low=-10, high=10, size=(5,1))
print(A)

# get natural log
print(math.log(10))
print(math.log(2.718))

# vectorized function
vector = np.array([2.718, 2, 2.718])
log = np.vectorize(lambda x: math.log(x)) 
print(log(vector))

a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(a * b)

print(np.subtract(a, b))
print(1 - a)

# getting all but first row of matrix

a = np.array([
    1,
    2,
    3,
])

print(a[1:])
