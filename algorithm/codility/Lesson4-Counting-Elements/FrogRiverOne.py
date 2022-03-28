from collections import Counter

def solution(X, A):
    print(A[0])
    check = [False] * X
    print(check)
    for idx, val in enumerate(A):
        check[val - 1] = True
        print(check)
        if not False in check:
            return idx
    return -1
if __name__ == "__main__":

    A = [2,2,2,2,2,2]
    X = 2
    print(solution(X, A))