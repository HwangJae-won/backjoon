#1026 보물
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s=0
for i in range(n):
    s += sorted(a)[i] * sorted(b, reverse=True)[i]
print(s)


