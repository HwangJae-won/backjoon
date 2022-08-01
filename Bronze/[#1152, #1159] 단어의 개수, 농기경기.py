#1152 단어의 개수
# 문장이 주어졌을 때 단어의 개수를 세는 프로그램 : 중복 시에도 카운트
sen = input()
print(len(sen.split()))

#1159 농구 경기
from collections import Counter
n= int(input())
player=[]
fn=[]
cnt =0
for i in range(n):
    name= input()
    player.append(name[0])‹
for i,j in Counter(player).items():
    if j >= 5:
        fn.append(i)
        cnt += 1
fn.sort()
fn
if cnt ==0:
    print("PREDAJA")
else:
    for i in fn:
        print(i, end='')