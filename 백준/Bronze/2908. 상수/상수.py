list_answer = list(map(int, input().split()))
# print(list_answer)

a = list_answer[0]
# print(a)
list_a = []
for i in str(a):
    list_a.append(i)
list_a.reverse()
# print(list_a)
new_a = (int(list_a[0]) * 100) + (int(list_a[1]) * 10) + int(list_a[2])
# print(new_a)

b = list_answer[1]
list_b = []
for i in str(b):
    list_b.append(i)
list_b.reverse()
new_b = (int(list_b[0]) * 100) + (int(list_b[1]) * 10) + int(list_b[2])
# print(new_b)

if new_a > new_b:
    print(new_a)
else:
    print(new_b)
