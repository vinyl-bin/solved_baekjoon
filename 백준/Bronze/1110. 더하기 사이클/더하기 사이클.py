num = int(input())

cur = num

if cur < 10:   # cur이 한 자리수 일때
    list_num1 = list(map(int, str(cur)))
    cur = list_num1[0]
else:          # cur이 두 자리수 일때
    list_num1 = list(map(int, str(cur)))
    cur = list_num1[0]+list_num1[1]
    
list_num2 = list(map(int, str(cur)))  #각 자리수끼리 더한 cur값을 자리수별로 리스트로 변환

if cur < 10:   # 각 자리수끼리 더한 cur값이 한 자리수 일때
    if num < 10:
        cur = list_num1[0]*10+list_num2[0]
    else:
        cur = list_num1[1]*10+list_num2[0]
else:
    if num < 10:
        cur = list_num1[0]*10+list_num2[1]
    else:
        cur = list_num1[1]*10+list_num2[1]

cnt = 1

while cur != num: #계속 바뀌는 수인 cur이 원래 입력한 값이 num과 같아야 반복문이 끝나므로 처음에는 cur=num이므로 반복문에 넣지 못하고 두번째부터 반복문을 실행함
    
    cur_origin = cur

    if cur < 10:   # cur이 한 자리수 일때
        list_num1 = list(map(int, str(cur)))
        cur = list_num1[0]
    else:          # cur이 두 자리수 일때
        list_num1 = list(map(int, str(cur)))
        cur = list_num1[0]+list_num1[1]
    
    list_num2 = list(map(int, str(cur)))  #각 자리수끼리 더한 cur값을 자리수별로 리스트로 변환

    if cur < 10:   # 각 자리수끼리 더한 cur값이 한 자리수 일때
        if cur_origin < 10:
            cur = list_num1[0]*10+list_num2[0]
        else:
            cur = list_num1[1]*10+list_num2[0]
    else:
        if cur_origin < 10:
            cur = list_num1[0]*10+list_num2[1]
        else:
            cur = list_num1[1]*10+list_num2[1]
    
    cnt += 1

print(cnt)