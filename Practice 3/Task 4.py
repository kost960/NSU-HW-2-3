R, K, N = list(map(float, input().split()))
full = (R + (K) / 100) * N
print(round(full), 'руб.', round((full % 1) * 100), 'коп.')
