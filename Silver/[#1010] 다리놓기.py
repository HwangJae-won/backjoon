#1010 다리 놓기: 조합문제로 풀 수 있다
import sys
import math
t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(math.factorial(m) // #(math.factorial(n) * math.factorial(m-n)))