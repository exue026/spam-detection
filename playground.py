import site
print(site.getsitepackages())

import numpy as np

A = ['one', 'two', 'three']
hashmap = dict(np.ndenumerate(A))

a = np.array([[1, 1], [2, 2], [3, 3]])
print(a)

bias = np.ones((a.shape[0], 1), dtype=int)
print(bias)

b = np.concatenate((bias, a), axis=1)
print(b)

A = np.random.uniform(low=-10, high=10, size=(5,1))
print(A)