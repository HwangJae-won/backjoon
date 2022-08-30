#1417 국회의원 선거
n = int(input())
li =[]
cnt =0
#각 후보별 투표수 list
for i in range(n):
    li.append(int(input()))
da = li[0] #다솜이는 기호 1번
other = li[1:]
#정렬하여 다솜 제외 유력 후보 찾기
other.sort(reverse=True)
if n == 1:
    print(0)
else:
    while other[0] >= da:
        da +=1
        other[0] -= 1
        cnt += 1
        other.sort(reverse=True)
    print(cnt)