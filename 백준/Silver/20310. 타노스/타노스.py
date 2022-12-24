num = input()

num_list = []
for i in str(num):
    num_list.append(i)

zero = num_list.count("0") // 2
one = num_list.count("1") // 2

for i in range(zero):
    num_list.pop(-num_list[::-1].index("0") - 1)
for j in range(one):
    num_list.pop(num_list.index("1"))
print("".join(num_list))

# 참고 블로그 https://jinho-study.tistory.com/983

# num0_list = []
# num1_list = []
# for i in range(len(num_list)):
#     if num_list[int(i)] == "0":
#         num0_list.append(num_list[i])
#     elif num_list[int(i)] == "1":
#         num1_list.append(num_list[i])

# final_list1 = []
# for i in range((len(num0_list)) // 2):
#     final_list1.append(num0_list[i])

# final_list2 = []
# for i in range((len(num1_list)) // 2):
#     final_list2.append(num1_list[i])


# final_list = []
# final_list = final_list1 + final_list2

# result = "".join(s for s in final_list)
# print("".join(final_list))
