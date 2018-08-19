import numpy as np

def Solve(maps, N, M):
    """
    only need to calculate M in [1,6] cases,
    6-4 can get period,
    if M > 4 and M % 2 == 0, case can base on 4
    if M > 5 and M % 2 == 1, case can base on 5

    hence when M<7,O(M * N^3)
    when M>=7,O(N^3)
    """
    if M == 0:
        return [[0 for i in range(N)] for j in range(N)]

    res = [[maps[i][j] for i in range(N)] for j in range(N)]
    if M == 1:
        return res
        
    # M = 2 is different，need to be calculate particularly,
    # start point can not include it start line index
    result = []
    for i in range(N):
        res_tmp = []
        for j in range(N):
            tmp = -1
            for t in range(N):
                if (t==i or t==j):
                    continue
                # print(str(i) + "," + str(t)+ " " + str(t) + "," + str(j) + " " + str(res[i][t]) + " " + str(maps[t][j]) )
                if res[i][t] + maps[t][j] < tmp or tmp < 0:
                    tmp = res[i][t] + maps[t][j]
            res_tmp.append(tmp)
            # print("-----------------")
        result.append(res_tmp)
        # print("********************")
    res = result
    if M < 3:
        return res
    # print(res)

    # calculate M=3, 4, 5, 6 record 4,5 as base case  6-4 calculate increament
    C = M - 2 if M < 6 else 4
    hahaha = []
    for _ in range(C):
        result = []
        for i in range(N):
            res_tmp = []
            for j in range(N):
                res_tmp.append( min([ res[i][t] + maps[t][j] for t in range(j) ]
                    + [ res[i][t] + maps[t][j] for t in range(j+1, N) ]) )
            result.append(res_tmp)
        res = result
        # print(res)
        hahaha.append(res)
    # print(len(hahaha))
    if M < 7:
        return hahaha[-1]
    increament = [[ hahaha[-1][r][c] - hahaha[-3][r][c] for c in range(N)] for r in range(N)]
    # print(increament)
    out_sol = []
    if M % 2 == 1:
        n = (M - 5) // 2
        # print(n)
        out_sol = [[ hahaha[-2][r][c] + n * increament[r][c] for c in range(N)] for r in range(N)]
    else:
        n = (M - 4) // 2
        # print(n)
        out_sol = [[ hahaha[-3][r][c] + n * increament[r][c] for c in range(N)] for r in range(N)]
    return out_sol


def solution(maps, N, M):
    if M == 0:
        return [[0 for i in range(N)] for j in range(N)]

    res = [[maps[i][j] for i in range(N)] for j in range(N)]
    if M == 1:
        return res


    result = []
    for i in range(N):
        res_tmp = []
        for j in range(N):
            tmp = -1
            for t in range(N):
                if (t==i or t==j):
                    continue
                # print(str(i) + "," + str(t)+ " " + str(t) + "," + str(j) + " " + str(res[i][t]) + " " + str(maps[t][j]) )
                if res[i][t] + maps[t][j] < tmp or tmp < 0:
                    tmp = res[i][t] + maps[t][j]
            res_tmp.append(tmp)
            # print("-----------------")
        result.append(res_tmp)
        # print("********************")
    res = result
    if M < 3:
        return res
    # print(res)

    # 计算M=3, 4, 5, 6记录4,5作为base case之后的增长来回摩擦, 6-4算增量

    # C = M - 2 if M < 6 else 5
    # hahaha = []
    for _ in range(M-2):
        result = []
        for i in range(N):
            res_tmp = []
            for j in range(N):
                res_tmp.append( min([ res[i][t] + maps[t][j] for t in range(j) ]
                    + [ res[i][t] + maps[t][j] for t in range(j+1, N) ]) )
            result.append(res_tmp)
        res = result
        # print(res)
        # hahaha.append(res)
    return res

if __name__ == '__main__':
    maps = [[0,2,3],[2,0,1],[3,1,0]]
    for M in range(2, 10):
        # print(M)
        result = Solve(maps, 3, M)
        print(result)
        # result = solution(maps, 3, M)
        # print(result)
