
def solution(name: str):

    """
    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,W,X,Y,Z
    """
    print(ord("J"))
    lst = [min(ord(n) - ord("A"), ord("Z")-ord(n)+1) for n in name]
    # [9, 4, 9, 12, 4, 13]
    # print(sum(lst))
    idx, answer = 0, 0
    print(lst)
    while True:
        answer += lst[idx]
        lst[idx] = 0

        if sum(lst) == 0:
            break

        left, right = 1, 1
        while lst[idx - left] == 0:
            left += 1

        while lst[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
        print(f"idx: {idx} , {answer}")

    return answer


if __name__ == "__main__":
    name = "JEROEN"
    solution(name)