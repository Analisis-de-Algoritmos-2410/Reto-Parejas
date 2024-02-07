import unittest
from mapSolution import mapSolution
from naive_solution import naive_solution
from n_log_n import n_log_n
from arrayLockUpSolution import arrayLockUpSolution
from factorial_solution import factorial_solution

class TestSolutionsMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.arrLU = [1, 9, 5, 0, 20, 4, 11, 16, 7]
        self.arr = [1, 9, 5, 0, 20, -4, 12, 16, 7]
        self.target = 12

    def test_arrayLockUp(self):
        ret = arrayLockUpSolution(self.arrLU, self.target)
        ret.sort()
        self.assertEqual(ret, [(1, 11), (5, 7)])
    
    def test_nlogn(self):
        ret = n_log_n(self.arr, self.target)
        ret.sort()
        self.assertEqual(ret, [(-4,16), (0,12), (5,7)])
    
    def test_naive(self):
        ret = naive_solution(self.arr, self.target)
        ret.sort()
        self.assertEqual(ret, [(-4,16), (0,12), (5,7)])

    def test_map(self):
        ret = mapSolution(self.arr, self.target)
        ret.sort()
        self.assertEqual(ret, [(-4,16), (0,12), (5,7)])

    def test_factorial(self):
        ret = factorial_solution(self.arr, self.target)
        ret.sort()
        self.assertEqual(ret, [(-4,16), (0,12), (5,7)])