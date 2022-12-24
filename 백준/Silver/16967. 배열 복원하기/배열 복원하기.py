H, W, X, Y = map(int, input().split())

B_array = [[0] * (W + Y) for _ in range(H + X)]

for i in range(H + X):
    B_array[i] = list(map(int, input().split()))

A_array = [[0] * W for _ in range(H)]  # 왜 [0]을 해야하는지?

for i in range(H):
    for j in range(W):
        A_array[i][j] = B_array[i][j]

for i in range(X, H):
    for j in range(Y, W):
        A_array[i][j] = B_array[i][j] - A_array[i - X][j - Y]

for i in range(H):
    for j in range(W):
        print(A_array[i][j], end=" ")
    print("")

# 참고 https://velog.io/@sugenius77/%EB%B0%B1%EC%A4%80Python-16967%EB%B2%88-%EB%B0%B0%EC%97%B4-%EB%B3%B5%EC%9B%90%ED%95%98%EA%B8%B0
