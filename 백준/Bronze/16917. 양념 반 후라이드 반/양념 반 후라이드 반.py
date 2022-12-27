souce_price, fried_price, half_price, want_souce, want_fried = map(int, input().split())
result = 0

while (want_souce > 0) or (want_fried > 0):
    if want_souce > want_fried:
        if souce_price >= (half_price * 2):
            want_souce -= 1
            # print(want_souce)
            result += half_price * 2
            # print(result)
        else:
            want_souce -= 1
            # print(want_souce)
            result += souce_price
            # print(result)
    elif want_souce < want_fried:
        if fried_price >= (half_price * 2):
            want_fried -= 1
            # print(want_fried)
            result += half_price * 2
            # print(result)
        else:
            want_fried -= 1
            # print(want_fried)
            result += fried_price
            # print(result)
    else:
        if (souce_price + fried_price) >= (half_price * 2):
            want_souce -= 1
            want_fried -= 1
            # print(want_souce, want_fried)
            result += half_price * 2
            # print(result)
        else:
            want_souce -= 1
            want_fried -= 1
            # print(want_souce, want_fried)
            result += souce_price + fried_price
            # print(result)

print(result)
