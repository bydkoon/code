

n, m = map(int, input().split())
print(n, m)

#N개의 화폐단위 정보를 입력받기 ex) 2,3,5
array = []

for i in range(n):
    array.append(int(input()))

#한번 계산된 결과를 저장하기 위한 DP테이블 초기화 
d = [10001] * (m+1)

#DP진행 (보텀업)
# array = [2,3,5]
d[0]= 0
for i in range(n): # n가지 화폐로 확인 ex) 3 
    for j in range(array[i], m+1): # 첫번째 배열 금액 i원 금액부터 m원화폐 까지확인 ex)7 
        if d[j - array[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

#계산된 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])


