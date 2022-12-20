import sys

goj, gab, panm = map(int, sys.stdin.readline().split())

if gab >= panm:
    point = -1
else:
    bi = goj
    point = 0
    point = bi // (panm - gab)
    point = point + 1

print(point)
