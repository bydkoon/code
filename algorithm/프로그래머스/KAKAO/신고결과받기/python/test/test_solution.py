import unittest
import sys
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__))))


class TestSolution(unittest.TestCase):
    
    def test_solution(self):
        H = ""
        answer = ""
        self.assertEqual(solution(H) , answer)



# unittest를 실행
if __name__ == '__main__':  
    unittest.main()
