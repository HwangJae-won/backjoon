#1173 운동
N, m , M, T, R = map(int, input().split())
time, init_N = 0, 0
stop = m
while init_N< N:
    #m + T 일 때 운동 불가
    if m +T > M:
        break
    # 운동
    if stop + T <= M:
        stop += T
        init_N += 1
    # 휴식
    else:
        stop =max(stop -R , m)
    time +=1

print(time if init_N == N else -1)


