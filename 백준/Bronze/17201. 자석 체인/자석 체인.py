N = int(input())
jasuk_array = list(map(int, input()))

# print(jasuk_array)


if jasuk_array[0] == 1:
    compare_array = [0 for _ in range(N * 2)]
    # print(compare_array)
    for k in range(N * 2):
        if k % 2 == 0:
            compare_array[k] = 1
        else:
            compare_array[k] = 2
    # print(compare_array)
    # print(jasuk_array == compare_array)
    if (jasuk_array == compare_array) == True:
        print("Yes")
    else:
        print("No")

if jasuk_array[0] == 2:
    compare_array = [0 for _ in range(N * 2)]
    # print(compare_array)
    for k in range(N * 2):
        if k % 2 == 0:
            compare_array[k] = 2
        else:
            compare_array[k] = 1
    # print(compare_array)
    if (jasuk_array == compare_array) == True:
        print("Yes")
    else:
        print("No")
