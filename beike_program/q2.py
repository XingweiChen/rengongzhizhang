n = int(input())

buf = [1 for _ in range(n ** 2)]
for i in range(2, 10000):
    buf[i] += 1
    if (buf[i]) == n:
        print(i)
        break
    for j in range(2, 10000):
        if i * j < n ** 2:
            buf[i * j] += 1
