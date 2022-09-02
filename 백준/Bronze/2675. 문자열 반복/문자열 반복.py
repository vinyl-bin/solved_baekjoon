N = int(input())

for i in range(N):
    input_list = list(input().split())
    # print(input_list)
    code = input_list[1]
    # print(code)
    code_list = []
    for j in str(code):
        code_list.append(j)
    # print(code_list)
    for voca in code_list:
        # print(voca)
        for rep in range(int(input_list[0])):
            print(voca, end="")
    print("")
