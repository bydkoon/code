# def fibo(x):
#     if x == 1 or x ==2:
#         return 1
#     return fibo(x-1)+fibo(x-2)

# print(fibo(4))

#탑다운 방식 일반적으론 동일하게 볼수있다. 프로그램 과정상 탑다운이 더 걸릴수있다.

#100개의 배열을 미리 할당을 받아둔다
d = [0] * 100

def fibo(x):
    #초기값이 1,2인경우 결과를 1로 반환한다.
    if x == 1 or x == 2:
        return 1

    #메모리 데이터에 0이아닌경우는 배열에서 이미 계산된 값을 반환한다ㅏ.
    if d[x] != 0:
        return d[x]
    #d메모리에 없을경우는 fibo 재귀호출 한다.    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

