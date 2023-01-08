import sys

M, N = map(int, sys.stdin.readline().split())

list_check = [True] * (N + 1)

list_check[0] = False
list_check[1] = False

for i in range(2, int(N**0.5) + 1):
    for j in range(i * 2, N + 1, i):
        list_check[j] = False

for k in range(M, N + 1):
    if list_check[k]:
        print(k)
