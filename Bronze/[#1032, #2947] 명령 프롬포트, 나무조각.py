#1032 명령 프롬프트
n = int(input())
w1 = list(input()) #비교 대상인 첫번째 문장
for i in range(n-1): #앞에서 하나 입력 받았으니까 n-1
    w2 =list(input())
    for j in range(len(w1)):
        if w1[j] != w2[j]: #리스트 내의 글자들 비교하여 다를 경우 ? 로 대체
            w1[j] = "?"
print(''.join(w1))

#2947 나무조각
import sys
nums = list(map(int, sys.stdin.readline().split(' ')))
while True:
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
      temp = nums[i]
      nums[i] = nums[i + 1]
      nums[i + 1] = temp
      print(' '.join(map(str, nums)))

  if nums == [1, 2, 3, 4, 5]: break