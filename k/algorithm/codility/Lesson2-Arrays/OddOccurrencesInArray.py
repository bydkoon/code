
from collections import Counter

def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    counter = Counter(A)
    new_dict = sorted(counter.items(), key=lambda x:x[1], reverse=True)
    last_dict = new_dict[len(new_dict) - 1:]
    return last_dict[0][0]


def solutions(A):
    if len(A) == 1:
        return A[0]

    A = sorted(A)
    print(A)
    for i in range(0, len(A), 2):
        if i + 1 == len(A):
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]


if __name__ == "__main__":
    A = [9, 3, 9, 3, 9, 7, 9] 
    print(solutions(A))