from collections import Counter

def solution(X, A):
    c = [0] * X
    s = 0
    for k, v in enumerate(A):
        if c[v-1] == 0:
            c[v-1] = 1
            s+=1
            if s == X:
                return k
    return -1
if __name__ == "__main__":

    A = [1, 3, 1, 4, 2, 3, 5, 4]
    X = 5
    print(solution(X, A))