
def solution(phone_number):
    phone_size = len(phone_number)
    phone_size -= 4
    answer = ""    
    if phone_size == 0:
        return "****"

    answer += ("*" * phone_size) +(phone_number[phone_size:])

    return answer