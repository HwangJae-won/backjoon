#1065 한수: 각 자리가 등차 수열을 이룰 때 한수
## 등차 수열: 연속된 두 개의 수의 차이가 일정
n = int(input())
han = 0
for i in range(1, n+1):
    if i < 100: ##99까지는 다 한수라고 할 수 있음
        han += 1
    else: #자리 수의 차이가 일정
        li = list(map(int, str(i)))
        if li[1] - li[0] == li[2] - li[1]:
            han+=1
print(han)