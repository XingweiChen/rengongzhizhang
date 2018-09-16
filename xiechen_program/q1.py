from math import log2

n = int(input())
data = dict()

pc, nc = 0, 0
for _ in range(n):
    k, v = input().split(",")
    v = v.strip()
    if k not in data:
        data[k] = [0, 1] if v == "1" else [1, 0]
    else:
        data[k][int(v)] += 1
    if v == "1":
        pc += 1
    else:
        nc += 1

pp = pc /(pc + nc)
np = nc / (pc + nc)

ori = pp * log2(pp) + np * log2(np)
for k in data:
    [v1, v2] = data[k]
    tot = (v1+v2)
    data[k] = [v1 / tot, v2 / tot, tot]
# print(data)
result = 0
for k in data:
    v = data[k]
    tmp = 0
    if v[0] != 0:
        tmp += v[0] * log2(v[0])
    if v[1] != 0:
        tmp += v[1] * log2(v[1])
    result += (v[2] / n) * tmp

print('%.2f'%(result - ori))
