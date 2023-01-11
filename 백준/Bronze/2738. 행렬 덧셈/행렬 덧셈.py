rows, cols = map(int, input().split())

arr1 = [list(map(int, input().split())) for i in range(rows)]
arr2 = [list(map(int, input().split())) for i in range(rows)]
arr_new = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        arr_new[i][j] = arr1[i][j] + arr2[i][j]
        print(arr_new[i][j], end=" ")
    print()
