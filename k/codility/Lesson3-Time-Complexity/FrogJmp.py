import math

def solution(X,Y,D):

    c = math.ceil((Y - X) / D)
    return c


if __name__ == "__main__":
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))