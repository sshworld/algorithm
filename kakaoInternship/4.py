

def solution(n, start, end, roads, traps):
    answer = 0

    check = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    checkPoint = [False for _ in range(n + 1)]
    checkPoint[0] = True
    checkPoint[start] = True

    for x, y, d in roads :
        check[x][y] = d

    def find(num) :
        
        if num == end and any(checkPoint): 
            return 0

        ret = float('inf')

        for i in range(len(check[num])) :
            x = check[num][i]
            if(check[num][i] != 0) :
                checkPoint[i] = True
                num = i
                if num in traps :
                    for i in range(len(check[num])) :
                        check[num][i], check[i][num] = check[i][num], check[num][i]
                ret = min(ret, find(num) + x)
                print(ret, x)
                checkPoint[i] = False
                if num in traps :
                    for i in range(len(check[num])) :
                        check[i][num], check[num][i] = check[num][i], check[i][num]


        return ret

    return find(start)


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))