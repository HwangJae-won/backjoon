#1158 요세푸스 문제 : 요세푸스 순열 -> K 번째 사람 제거하고 이를 순열로 출력하기
n,k = map(int, input().split())
num = list(range(1, n+1))
idx = k-1
ans=[]
while True:
    ans.append(num[idx])
    num = num[:idx] +num[idx+1:] #현재 idx 제거
    if not num:
        break
    idx =(idx +k-1) % len(num)
print('<' +', '.join(list(map(str, ans)))+'>')

