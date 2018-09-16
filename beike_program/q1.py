n = int(input())
t = []
for i in range(n):
    in1, in2 = input().split()
    t.append((int(in1), int(in1) + int(in2), i))

t = sorted(t, key=lambda x: x[0])
result = [-1 for _ in range(n)]

for i in range(len(t)):
    cnt = 1
    for j in range(i+1, len(t)):
        if t[j][0] >= t[i][1]:
            break
        if t[i][0] < t[j][0]:
            cnt += 1
    result[t[i][2]] = str(cnt)
print(" ".join(result))
