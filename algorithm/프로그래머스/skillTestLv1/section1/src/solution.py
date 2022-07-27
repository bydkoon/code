
def solution(s, n):
    answer = ""
    for i in s:
        if ord(i) == 32:
            answer += chr(ord(i))
        elif i.isupper():
            answer += chr(ord("A") + (ord(i) + n - ord("A")) % 26)
        else:
            answer += chr(ord("a") + (ord(i) + n - ord("a")) % 26)
        
    return answer

