
from collections import Counter

def solution(A):
    A.sort()
    counter = Counter(A)
    print(counter)



if __name__ == "__main__":
    A = [9, 3, 9, 3, 9, 7, 9] 
    print(solution(A))