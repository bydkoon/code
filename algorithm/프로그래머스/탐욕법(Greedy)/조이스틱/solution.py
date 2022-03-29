
def solution(name: str):

    """
    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,W,X,Y,Z
    """

    lst = [min(ord(n) - ord("A"), ord("Z")-ord(n)+1) for n in name]
    # [9, 4, 9, 12, 4, 13]
    print(sum(lst))
    cnt = 0
    loc = 0
    print(lst)
    while True:
        cnt += lst[loc]
        lst[loc] = 0
        if sum(lst) == 0:
            break
        left = 1
        right = 1
        while lst[loc + right] == 0:
            right += 1

        while lst[loc - left] == 0:
            left += 1
        if left >= right:
            loc += right
            cnt += right
        else:
            loc -= left
            cnt += left

    return cnt


if __name__ == "__main__":
    name = "JEROEN"
    solution(name)