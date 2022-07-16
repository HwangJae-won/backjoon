#2480 주사위 세 개
n1, n2, n3 = map(int, input().split())
if n1 == n2 == n3:
    print(10000 + n1*1000)
elif n1 == n2 or n2 == n3 :
    print(1000 + n2 * 100)
elif n1 == n3:
    print(1000+ n1 *100 )
else:
    print(max(n1,n2,n3) *100)