#2530 인공지능 시계
h , m, s = map(int , input().split())
d = int(input())

#초 계산
s += d % 60 #나머지
d = d//60
if s>= 60: #초가 60을 넘어갈 경우, 60 뺘주고 분 추가
    s-=60
    m +=1
#분 계산
m+= d%60 #나머지
d = d//60
if m >= 60:
    m-= 60
    h += 1
#시 계산
h+산 d%24
if h>= 24:
    h-= 24

print(h,m,s)
