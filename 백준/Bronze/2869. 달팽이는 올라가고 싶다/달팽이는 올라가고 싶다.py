import sys

day, night, miter = map(int, sys.stdin.readline().split())
result = 0

result = ((miter - day) / (day - night)) + 1

if (result % 1) == 0:
    result = int(result)
else:
    result = int(result) + 1

print(result)