import sys

# M = int(input())
# N = int(input())
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sosu_list = [0]

for i in range(M, N + 1):
    count = 0
    for j in range(1, N + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        sosu_list.append(i)
        # print(i)
sum_list = sum(sosu_list)
if sum_list == 0:
    print("-1")
else:
    print(sum_list)
    print(sosu_list[1])
