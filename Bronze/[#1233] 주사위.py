#1233 주사위
s1, s2, s3 = map(int, input().split())
sum=[0] *81
sum
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            sum[i+j+k] +=1
print(sum.index(max(sum)))

