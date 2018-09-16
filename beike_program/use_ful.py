# 按2个小数位数输出
print ('%.2f' % y)


n, m, x = raw_input().split()
p = raw_input()

# 转float
n, m, x = float(n), float(m), float(x)
p = float(p)

# 转int
n, m, x = int(n), int(m), int(x)
p= int(p)

# 循环输入
while(n):
    n -= 1
    inp = raw_input()

print (x, end = "")

n, m, x = input().split()
p = input()



"""
n, m = raw_input().split()
n, m = int(n), int(m)
buf = [0 for _ in range(n)]
buf[-1], buf[1] = 1, 1
for i in range(m - 1):
  tmp = [0 for _ in range(n)]
  for j in range(n):
    if buf[j] > 0:
      tmp[-1 if j-1 < 0 else j-1] += buf[j]
      tmp[0 if j+1>n-1 else j+1] += buf[j]
  buf = tmp
print(buf)
print(buf[0])
"""


"""
n, m, x = raw_input().split()
p, q = raw_input().split()

n, m, x = float(n), float(m), float(x)
p, q = float(p), float(q)

y = x / (n + 1) / ( q / p - n/ (n+1) )
print y

if y  < 1:
  y = 1
if y > m:
  y = m

print '%.2f' % y

"""
