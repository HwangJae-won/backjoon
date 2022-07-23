# 1284 집주소
while True:
    n = str(input())
    if n == '0':
        break

    w = len(n) +1
    for i in n:
        if i == '0':
            w += 4
        elif i == '1':
            w+= 2
        else:
            w+= 3
    print(w)

#1547 공
m = int(input())
li=[1,2,3]
for _ in range(m):
    x,y = map(int, input().split())
    X =li.index(x); Y = li.index(y)
    #li[li.index(x)],li[li.index(y)] = li[li.index(y)],li[li.index(x)]
    li[X],li[Y] = li[Y],li[X]
print(li[0])


