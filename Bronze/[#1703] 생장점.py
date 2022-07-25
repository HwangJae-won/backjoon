#1703 생장점
while True:
    li = list(map(int, input().split()))
    leaf= 1
    if li[0] ==0:
        break

    for i in range(1, len(li), 2):
        leaf = leaf * li[i]-li[i+1]
    print(leaf)