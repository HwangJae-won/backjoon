#1297 TV 크기
d, h, w = map(int, input().split())
ratio = d/ (((h**2 + w**2))**(1/2))
print(int(ratio*h),int(ratio*w) )

#2386 도비의 영어공부
while True:
    a= input()
    if a == "#":
        break
    word = a[0]
    sen = a[1:].lower() #소문자 변환 안해주면 숫자가 달라진다!
    print(word, sen.count(word))
