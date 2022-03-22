from collections import Counter


def solution(A):
    if len(A) == 0:
        result = 1
    else :
        result = sum(range(1, len(A)+2)) - sum(A)
    return result




if __name__ == "__main__":
    A = dict()
    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5

    solution(A)