T = int(input())

for k in range(T):
    H = int(input())
    W = int(input())
    list_temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    del list_temp[W:]
    # print(list_temp)
    for i in range(H):
        for j in range(W):
            if j == 0:
                list_temp[0] = list_temp[0]
            else:
                list_temp[j] = list_temp[j - 1] + list_temp[j]

    print(list_temp[W - 1])