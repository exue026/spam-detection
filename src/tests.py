import unittest
import math
import numpy as np

from compute import cost,init_params,h, Log

class Tests(unittest.TestCase):
    def test_cost(self):
        X = np.array([
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]) 
        theta = np.array([
            -1,
            0,
            1
        ])
        y = np.array([
            1,
            1,
            0
        ])
        self.assertAlmostEqual(cost(h, X, theta, y, 0), -math.log(0.5))
        
    def test_vectorized_log(self):
        a = Log(np.array([[2.71828, 2.71828], [2.71828, 2.71828]]))
        expected = np.array([[0.999999, 0.999999], [0.999999, 0.999999]])
        np.testing.assert_array_almost_equal(a, expected)
    
    def test_vectorized_log2(self):
        a = Log(np.array([1, 1, 1]))
        print(a)


if __name__ == '__main__':
    unittest.main()