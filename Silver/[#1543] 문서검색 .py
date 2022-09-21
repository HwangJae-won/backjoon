#1543 문서 검색
doc = input() ; key = input()
cnt, index = 0,0
for i in range(len(doc)):
    if index>i:
        continue
    if key == doc[i: i+len(key)]:
        cnt +=1
        index = i +len(key)
print(cnt)

