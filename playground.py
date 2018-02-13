import site
print(site.getsitepackages())

import numpy as np

A = ['one', 'two', 'three']
hashmap = dict(np.ndenumerate(A))
print(hashmap[1])
    