#4493 가위 바위 보 ?
for _ in range(int(input())):
    n= int(input())
    a_win = b_win = 0
    for i in range(n):
        a, b = input().split()
        if a == b:
            continue
        elif (a == 'R' and b == 'S') or (a =='P' and b == 'R') or (a=='S' and b=='P'):
            a_win += 1
        else:
            b_win += 1
    if a_win < b_win:
        print("Player2")
    elif a_win > b_win:
        print("Player1")
    else:
        print("TIE")
 