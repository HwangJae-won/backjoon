#1251 단어 나누기
word = input() #리스트를 씌워 한 단어씩 받기
ans =[] #여러개의 단어 조합이 들어갈 리스트
#반복문을 활용하여 3개의 단어로 나누기
for i in range(1, len(word)):
    a = word[:i][::-1]
    for j in range(i, len(word)-1):
        b = word[i:j+1][::-1]
        c = word[j+1:][::-1]
        ans.append(a+b+c)
ans.sort() #문자열도 정렬 가능
print(ans[0])