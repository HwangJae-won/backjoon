#1475 방 번호
n = input()
li= [0] * 10
cnt = 0
for i in n:
    if i =='6' or i =='9':
        cnt +=1
    else:
        li[int(i)] +=1

if cnt %2 ==0:
    cnt = cnt //2
else:
    cnt = cnt //2 + 1

li[6] = cnt
print(max(li))



