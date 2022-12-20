import sys

num = sys.stdin.readline()

for i in range(int(num)):
    H, W, N = map(int, sys.stdin.readline().split())
    room = 0
    if H >= N:
        room = 100 * N + 1
    else:
        if (N % H) == 0:
            tem_W = N // H
            tem_H = H

            room = 100 * tem_H + tem_W
        else:
            tem_W = N // H
            tem_W += 1
            tem_H = N % H

            room = 100 * tem_H + tem_W

    print(room)