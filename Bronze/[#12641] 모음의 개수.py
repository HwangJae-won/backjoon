## 12641
#내가 구하고자 하는 값이 조건이 명확하지 않음 : for 문 대신 while 사용
# 그냥 메모리 오래 걸릴 것 같아서 while 사용하기
while 1:
    sentence = input()
    if sentence == '#': #'#' 등장하면 문장 종료
        break
    cnt = 0
    for i in sentence:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)


