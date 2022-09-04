from string import ascii_uppercase

voca_list = list(map(str, input()))
# print(voca_list)

alpha_list = list(ascii_uppercase)
# print(alpha_list)
all_time = 0
for i in range(len(voca_list)):
    num = alpha_list.index(voca_list[i])
    # print(num)
    if num >= 15 and num <= 18:
        time = int(8)
    elif num >= 19 and num <= 21:
        time = int(9)
    elif num >= 22 and num <= 25:
        time = int(10)
    elif num <= 14 and num >= 0:
        time = int(num / 3) + 3

    all_time += time
    # print(time)
print(all_time)
