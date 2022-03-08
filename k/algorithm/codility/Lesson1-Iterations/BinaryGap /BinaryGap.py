def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    print(binary)
    top = 0
    cnt = 0
    for idx in binary:
        if idx == '1':
            if cnt > 0:
                if top < cnt:
                    top = cnt
                    cnt = 0
                else:
                    cnt = 0
        else:
            cnt += 1

    return top


if __name__ == '__main__':
    print(solution(2041))