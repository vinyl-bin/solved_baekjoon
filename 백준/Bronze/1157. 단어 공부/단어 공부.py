from collections import Counter

string_voca = input()
upper_string_voca = string_voca.upper()
upper_list = list(map(str, upper_string_voca))

count_voca_dict = Counter(upper_list)

values_list = count_voca_dict.values()
max_num = max(values_list)

list_key = []
for key, value in count_voca_dict.items():
    if value == max_num:
        a = key
        list_key.append(a)
# print(list_key)

if len(list_key) == 1:
    print(list_key[0])
else:
    print("?")