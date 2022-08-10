#1110 더하기 사이클
##런타임 에러 ㅠ ㅠ
n= input()
number= n
cnt =0

while True:
    if len(number) ==1:
        number = "0"+ num
    new=str(int(number[0]) + int(number[1]))
    number = number[-1] + new[-1]
    cnt+=1
    if number == n :
        print(cnt)
        break

##숫자열로 바라보자
n= int(input())
num = n
cnt=0
while True:
    a = num // 10
    b= num %10
    c= (a+b)%10
    num = (b*10) +c

    cnt +=1
    if num == n:
        break
print(cnt)

