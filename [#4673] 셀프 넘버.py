#4673 셀프 넘버
#숫자 집합 생성
num_set = set(range(1, 10001))
new = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    new.add(i)

self_num = sorted(num_set - new)
for i in self_num:
    print(i)
