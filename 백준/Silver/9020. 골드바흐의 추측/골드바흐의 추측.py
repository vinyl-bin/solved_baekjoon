# import sys

# N = int(sys.stdin.readline())
# new_sosu_list = []
# for _ in range(N):
#     num = int(sys.stdin.readline())

#     sosu_list = [True] * (num + 1)
#     sosu_list[0] = False
#     sosu_list[1] = False

#     for i in range(2, int(num**0.5) + 1):
#         for j in range(i * 2, num + 1, i):
#             sosu_list[j] = False

#     for k in range(2, num + 1):
#         if sosu_list[k]:
#             new_sosu_list.append(k)
#     # print(new_sosu_list)

#     for l in new_sosu_list:
#         other = num - l
#         if other in new_sosu_list:
#             print(l, end=" ")
#             print(other)
#             break


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())

    a, b = n // 2, n // 2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
