#3046 R2
r1 , s = map(int, input().split())
print(2 * s -r1)

#2742 기찍 N
n = int(input())
for i in range(0,n,1):
    print(n-i)

#1085 직사각형에서 탈출
x,y,w,h = map(int, input().split())
print(min(w-x, h-y, x, y))

#1247 부호: 입력이 많아 반복문으로 불러오면 타임에러 날 것 같음
import sys
for _ in range(3):
    N = int(sys. stdin.readline())
    n_list=[]
    for i in range(N):
        n_list.append(int(sys. stdin.readline()))

    if sum(n_list) == 0 :
        print("0")
    elif sum(n_list) > 0:
        print("+")
    else:
        print("-")
