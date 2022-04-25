
def solution(A):
    a = list(set(A))
    if len(a) != len(A):
        return 0
    a.sort()
    count = 1
    for i in a:
        if count == i:
            result =1
            count +=1
        else:
            result = 0
            break
    return result 


if __name__ == "__main__":
    A = dict()
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
    
    print(solution(A))


