#1837 암호제작: 에라토스테네스의 체 (소수 판별 알고리즘)
p , k = map(int, input().split())
li = [1]*k
for i in range(2, int(k**0.5)+1):
    if li[i] ==1:
        for j in range(i+i, k, i):
            li[j] =0

prime =[i for i in range(2, k) if li[i] ==1]

good, bad = 1, 0
for n in prime:
    if p%n ==0:
        good, bad = 0,n
        break

print("GOOD" if good else f"BAD {bad}")

#2010 플러그
import sys
n = int(sys.stdin.readline())
e = 1
for i in range(n):
    e +=  int(sys.stdin.readline())-1
print(e)