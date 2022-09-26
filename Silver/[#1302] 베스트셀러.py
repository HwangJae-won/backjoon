#1302 베스트 셀러
n = int(input())
li=[]
for i in range(n):
    li.append(input())
print(max(li))
### 이렇게 하면 따옴표도 함께 출력###

### 
import sys
from collections import defaultdict
input = sys.stdin.readline

books = defaultdict(int)
n = int(input())

for _ in range(n):
    book = input().rstrip()
    books[book] += 1

books = sorted(books.items())
print(sorted(books, key = lambda x : x[1], reverse = True)[0][0])