import sys

N = int(sys.stdin.readline())
list_mul = []
count = 0
for j in range(N):
    for i in range(2, N + 1):
        if N % i == 0:
            list_mul.append(i)
            N = N // i
            count += 1
            # print(N)
            break

    if N == 1:
        break

# print(list_mul)
for k in range(count):
    print(list_mul[k])
