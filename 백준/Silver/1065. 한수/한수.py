def hansu(num):
    num_cnt = 0
    num_list = []
    for i in range(1,(num+1)):
        num_list = list(map(int, str(i)))

        if i < 100:
            num_cnt += 1
        
        elif i >= 100 and i < 10000:
            if num_list[0]-num_list[1] == num_list[1]-num_list[2]:
                num_cnt += 1
        
    return num_cnt

x = int(input())
print(hansu(x))