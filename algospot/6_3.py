from itertools import combinations



# for i in range (c) :
#     n.append(list(map(int, input().split(' '))))

# for i in range (c) :
#     m.append(list(map(str, input().split(' '))))
#     for j in range(len(m[i])) :
#         mList.append(m[i][j*2:(j*2)+1+1])

# for i in range(c) :
#     dp[i] = [0 for _ in range(m[i] / 2 - 1)]

def findFriend(n, pairs, taken) :

    if(sum(taken) == n) :
        return 1

    # 이부분을 생각 못함..
    for i in range(n) :
        if (not taken[i]) :
            break

    count = 0

    for j in range(n) :
        if(not taken[j] and pairs[i][j]) :
            taken[i] = taken[j] = True
            count += findFriend(n, pairs, taken)
            taken[i] = taken[j] = False
    
    return count

def main() :
    c = int(input())

    count = [0 for _ in range(c)]

    for index in range(c) :
        
        n, m = map(int, input().split())

        taken = [False] * n
        
        pairs = [[0] * n for _ in range(n)]

        friend = list(map(int, input().split()))

        for i in range(m) :
            p = friend[2 * i]
            q = friend[2 * i + 1]

            pairs[p][q] = pairs[q][p] = 1
        
        count[index] = findFriend(n, pairs, taken)

    print(count)

main()
               
