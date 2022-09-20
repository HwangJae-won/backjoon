#1920 수 찾기
#숫자 입력 받기
n = int(input())
li_n= list(map(int,input().split()))
m = int(input())
li_m= list(map(int,input().split()))

for i in range(len(li_m)):
    if li_n.__contains__(li_m[i]):
        print(1)
    else:
        print(0)
############ 시간초과 발생 ###############
n = int(input())
li_n= list(map(int,input().split()))
m = int(input())
li_m= list(map(int,input().split()))
li_n.sort()
#이분 탐색 문제
def binary(i):
    first = 0
    end = n - 1
    while first <= end:
        mid = (first + end) // 2
        if li_n[mid] == i:
            return True
        if i < li_n[mid]:
            end = mid - 1
        elif i > li_n[mid]:
            first = mid + 1
for i in range(m):
    if binary(li_m[i]):
        print(1)
    else:
        print(0)

