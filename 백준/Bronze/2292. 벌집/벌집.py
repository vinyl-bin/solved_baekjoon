num = int(input())
result = 0

if num == 1:
    result = 1

elif ((num - 1) % 6) == 0:
    mul = 0
    num -= 1
    while 1:
        mul += 1
        num = num - (6 * mul)

        if num <= 0:
            break
    result = mul + 1

else:
    mul = 0
    while 1:
        mul += 1
        num = num - (6 * mul)

        if num <= 0:
            break
    result = mul + 1

print(result)