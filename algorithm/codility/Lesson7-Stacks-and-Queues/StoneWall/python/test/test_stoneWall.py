# import sys
# sys.path.append('/Users/k/algorithm/algorithm/codility/Lesson7-Stacks-and-Queues/StoneWall/python/src')
# print(sys.path)

import unittest

import sys
from os import path
print(path.dirname( path.dirname( path.abspath(__file__) ) ))
sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))

from src.stoneWall import solution


class TestSolution(unittest.TestCase):
    
    def test_solution(self):
        H = [8,8,5,7,9,8,7,4,8]
        answer = 7
        self.assertEqual(solution(H) , answer)



# unittest를 실행
if __name__ == '__main__':  
    
    unittest.main()