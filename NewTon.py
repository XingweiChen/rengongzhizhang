import random

def newton(g, g_k, g_kk, delta = 0.55, epislon = 0.001, sigma = 0.4):
    x = random.randint(1, 100)
    while(abs(g_k(x)) > epislon):
        dk = - g_k(x) / g_kk(x)
        print(g_k(x), x)
        m, mk = 0, 0
        while(m < 20) :
            left = g(x + delta ** m * dk);
            right = g(x) + sigma * delta ** m * g_k(x) * dk
            if(left <= right):
                mk = m
                break
            m += 1
        x = x + delta ** mk * dk
    return g(x)
def g(x):
    return x ** 2 - 3 * x + 1

def g_k(x):
    return 2 * x - 3

def g_kk(x):
    return 2

if __name__ == '__main__':
    print(newton(g, g_k, g_kk, 0.1) + 1 / 4)
