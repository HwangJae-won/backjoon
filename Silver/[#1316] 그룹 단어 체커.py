#1316 그룹 단어 체커
# 그룹 단어 : 각 문자가 연속해서 나타나는 경우
# 연속되지 않은 곳에서 해당 단어가 등장할 경우 그룹 단어가 아니라고 할 수 있음 !
cnt= 0
n = int(input())
for i in range(n):
    w = input() #n번 돌면서 단어 입력 받기
    for j in range(len(w)-1):
        if w[j] != w[j+1]:
            new = w[j+1:]
            if w[j] in new:
                cnt -=1
                break
    cnt += 1
print(cnt)
