"""

"""
def solution(A):
    A.sort()
    distict = 0
    # [1,1,1,2,2,3]
    N = len(A)

    if N == 0: 
        return 0

    count = 1
    for i in range(1, N):
        if A[i-1] != A[i]:
            count += 1
    return count

if __name__ == "__main__":

    A = [2,1,1,2,3,1]
    print(solution(A))


