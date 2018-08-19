from guangming_xiaoxue import Solve

if __name__ == "__main__":
    N = int(raw_input())
    M = int(raw_input())
    tp = raw_input()
    maps = []
    for i in range(N):
        tmp = raw_input().split()
        for j in range(N):
            tmp[j] = int(tmp[j])
        maps.append(tmp)

    print(maps)
    result = Solve(maps, N, M)
    print(result)
