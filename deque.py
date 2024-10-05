from collections import deque

n, m = map(int, input().split(' '))
toPop = map(int, input().split(' '))

dq = deque(range(1,n+1))

for i in toPop: