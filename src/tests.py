import unittest
import numpy as np

from compute import cost,init_params,h, Log

class Tests(unittest.TestCase):
    def test_cost(self):
        self.assertEqual(1, 1)
        
    def test_vectorized_log(self):
        a = Log(np.array([[2.71828, 2.71828], [2.71828, 2.71828]]))
        expected = np.array([[0.999999, 0.999999], [0.999999, 0.999999]])
        np.testing.assert_array_almost_equal(a, expected)


if __name__ == '__main__':
    unittest.main()