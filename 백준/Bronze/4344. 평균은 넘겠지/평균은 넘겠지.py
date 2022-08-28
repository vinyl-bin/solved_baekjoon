C = int(input())

for _ in range(C):
    list_s = list(map(int, input().split()))
    N = list_s[0]
    del list_s[0]
    list_sum = sum(list_s)
    average = list_sum/N
    num = 0
    for i in range(len(list_s)):
        if  list_s[i] > average:
            num += 1
    y = "{:.3f}".format((num/N)*100)
    print(y+"%")
