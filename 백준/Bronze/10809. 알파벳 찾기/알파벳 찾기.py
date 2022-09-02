from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
# print(alphabet_list, len(alphabet_list), sep=",")
voca_list = list(map(str, input()))

result_list = [-1 for _ in range(26)]
# print(result_list)

for voca in voca_list:
    voca_index = voca_list.index(voca)  # 단어의 알파벳 순서대로 인덱스 숫자를 얻는다.
    voca_alp_index = alphabet_list.index(voca)
    # print(voca_index, voca_alp_index)
    result_list[voca_alp_index] = voca_index

for i in result_list:
    print(i, end=" ")
