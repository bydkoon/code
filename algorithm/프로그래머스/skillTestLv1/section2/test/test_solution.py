import unittest
import sys
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__))))


class TestSolution(unittest.TestCase):
    
    def test_solution(d, budget):
        answer = 0
        self.assertEqual(solution(d,budget) , answer)



# unittest를 실행
if __name__ == '__main__':  
    unittest.main()
