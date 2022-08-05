#1371 가장 많은 글자
# 아스키코드값으로 문자열 처리 가능
import sys
ans =[0] *26 #0으로 채워진 빈 리스트 만들기
sen = sys.stdin .read()
for i in sen:
    if i.islower():
        ans[ord(i) - 97] +=1
for i in range(len(ans)):
    if ans[i] ==max(ans):
        print(chr(97+i),end='')

