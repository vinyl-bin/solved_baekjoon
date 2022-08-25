N = int(input())

for _ in range(N):
    list_ox = list(input())
    score = 0
    sum_score = 0
    
    for i in list_ox:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)