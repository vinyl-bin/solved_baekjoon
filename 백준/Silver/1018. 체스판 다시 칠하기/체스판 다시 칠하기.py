row, column = map(int, input().split())  # row 세로, column 가로

origin_list = list()
# for i in range(row):
#     origin_list.append(input())
count = []

for _ in range(row):
    origin_list.append(input())

# print(origin_list)

for a in range(row - 7):
    for b in range(column - 7):
        start_w = 0
        start_b = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if origin_list[i][j] != "W":
                        start_w += 1
                    if origin_list[i][j] != "B":
                        start_b += 1
                    else:
                        start_w += 0
                        start_b += 0
                else:
                    if origin_list[i][j] == "W":
                        start_w += 1
                    if origin_list[i][j] == "B":
                        start_b += 1
                    else:
                        start_w += 0
                        start_b += 0
        count.append(min(start_w, start_b))

print(min(count))

# print("start_w:", start_w)
# print("start_b:", start_b)

# result = min(start_w, start_b)

# print(result)
