def solution(A):
    result = 0
    count = 0
    for i in A:
        if i == 1 and count == 0:
            continue
        elif i == 0:
            count += 1
        elif i == 1:
            result += count

    if result > 1000000000:
        return -1
    return result

if __name__ == "__main__":

    A = [0,1,0,1,1]
   
    print(solution(A))

