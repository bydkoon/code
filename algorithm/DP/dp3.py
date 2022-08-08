#보텀업 개미전사 문제


# 정수 n을 입력 받는다.
n = int(input())



array = list(map(int, input().split()))
#조건만큼 할당 해준다.
d = [0] * 100

# dp 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0] , array[1])

for i in range(2,n):
	d[i] = max(d[i-1] , d[i-2] + array[i])

print(d[n-1])

