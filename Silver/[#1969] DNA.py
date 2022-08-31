#1969 DNA
n, m = map(int,input().split())
li =[]
#문자열을 list 형식으로 받아서 비교하기
for i in range(n):
    li.append(list(map(str, input())))

cnt, ha = 0,0
result=''
for i in range(m):
    a,c,g,t =0,0,0,0
    for j in range(n):
        if li[j][i] =="T":
            t +=1
        elif li[j][i] =="A":
            a+=1
        elif li[j][i] =="G":
            g += 1
        elif li[j][i] == "C":
            c +=1
    if max(a,c,g,t) ==a:
        result += "A"
        ha += c+g+t
    elif max(a, c, g, t) == c:
        result += 'C'
        ha += a + g + t
    elif max(a, c, g, t) == g:
        result += 'G'
        ha += a + c + t
    elif max(a, c, g, t) == t:
        result += 'T'
        ha += c + g + a
print(result)
print(ha)