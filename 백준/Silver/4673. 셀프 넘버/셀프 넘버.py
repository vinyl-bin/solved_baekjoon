number = list(range(1, 10001))

remove_list = []
for remove_num in number:
    for num in str(remove_num):
        remove_num += int(num)
    if remove_num <= 10000:
        remove_list.append(remove_num)

for i_num in set(remove_list):
    number.remove(i_num)

for i in number:
    print(i)
