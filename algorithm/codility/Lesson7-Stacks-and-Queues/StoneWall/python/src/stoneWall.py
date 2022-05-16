

def solution(H: list)-> int:
    
    stack = []
    count = 0

    for h in H:

        while stack and stack[-1] > h:
            stack.pop()

        if not stack or stack[-1] < h:
            count += 1
            stack.append(h)
        
    return count






