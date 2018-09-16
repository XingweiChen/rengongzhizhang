from collections import Counter
from math import log2

p_dist = input().split()
q_dist = input().split()

num_p = len(p_dist)
num_q = len(q_dist)

p_dic = dict(Counter(p_dist))
q_dic = dict(Counter(q_dist))

N = max(len(p_dic), len(q_dic))

result = 0
for i in range(N):
    p = p_dic[str(i+1)] / num_p if str(i+1) in p_dic else 0
    q = q_dic[str(i+1)] / num_q
    result += p * log2(p / q)
print('%.2f' % result)
