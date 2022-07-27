import unittest
import sys

from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__))))

from src.solution import solution

class TestSolution(unittest.TestCase):
    
    def test_solution(self):
        s = "z"
        n = 1
        answer = "a"
        self.assertEqual(solution(s,n) , answer)



# unittest를 실행
if __name__ == '__main__':  
    unittest.main()
