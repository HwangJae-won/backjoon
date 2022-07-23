#2845 파티가 끝나고 난 뒤
p, w = map(int, input().split())
n1,n2,n3,n4,n5 = map(int, input().split())
sum=p*w
print( n1-sum ,  n2-sum,  n3-sum, n4-sum, n5-sum )

"""
- input을 2번 정의하지 말자 ! 그렇게 비효율적일 수가 없는 행위..
    =>  labmbda 로 정의한 후 입력 받기 
- 반복문은 최대한 한 문장으로 하도록 
a,b=map(int,input().split())
print(*[i-a*b for i in map(int,input().split())])
"""
