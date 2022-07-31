
def solution(phone_number):
    phone_size = len(phone_number)
    phone_size -= 4
    if phone_size == 0:
        return "****"
    answer = ""

    answer += "*" * phone_size
    answer += (phone_number[phone_size:])
    return answer