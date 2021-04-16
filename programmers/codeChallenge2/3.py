
def find(a, edges, n) :

    if a == [0 for _ in range(len(a))] :
        return 0

    ret = 0

    for i in range(len(edges)):


        n += 1
        ret += find(a, edges, n)

    return ret

def solution(a, edges):
    

    answer = find(a, edges, 0)
        
    return answer



    # an = sorted(edges)

    # dp = [0 for _ in range(len(a))]

    # for x, y in an :
    #     if dp[x] == 0 and dp[y] == 0 :
    #         dp[x] += 1
    #         dp[y] += 1
    #     elif dp[x] == 0 and dp[y] > 0 :
    #         if max(dp) == dp[y] :
    #             dp[y] += 1
    #         dp[x] = dp[y] + 1
    #     elif dp[y] == 0 and dp[x] > 0 :
    #         if max(dp) == dp[x] :
    #             dp[x] += 1
    #         dp[y] = dp[x] + 1
    #     print(dp)

    # print(dp.index(max(dp)))

    # # for i in range(len(edges)) :