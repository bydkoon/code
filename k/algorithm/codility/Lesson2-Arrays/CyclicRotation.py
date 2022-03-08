def solution(A, K):
    # write your code in Python 3.6
    if len(A) > 0:

        if len(A) == K:
            return A

        for i in range(K, 0, -1):
            A.insert(0, A.pop())
        return A
    else:
        return []
if __name__ == '__main__':
    print(solution([3, 8, 9, 7, 6],3))