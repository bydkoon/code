import unittest
import sys
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__))))
from .. import solution


class TestSolution(unittest.TestCase):
    
    def test_solution(self):
        phone_number="01033334444"
        answer = "*******4444"
        self.assertEqual(solution(phone_number) , answer)


# unittest를 실행
if __name__ == '__main__':  
    unittest.main()
