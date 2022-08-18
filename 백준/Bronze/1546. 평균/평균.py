N = int(input())

List = list(map(int,input().split()))

M = max(List)
new_List = []
for i in range(N):
    a = List[i]/M*100
    new_List.append(a)

print(sum(new_List)/N)
