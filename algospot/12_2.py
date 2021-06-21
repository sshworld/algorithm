import math

def main() :
    
    c = int(input())

    ans = []

    for _ in range(c) :

        n = int(input())

        base = [list(map(float, input().split())) for _ in range(n)]

        dp = [float('inf') for _ in range(len(base) - 1)]

        for i in range(len(base) - 1) :
            
            x, y = base[i]

            for j in range(i + 1, len(base)) :
                p, q = base[j]

                distance = math.sqrt((x - p) * (x - p) + (y - q) * (y - q))

                dp[i] = min(dp[i], distance)


        ans.append(max(dp))

    for answer in ans :
        print(answer)

main()
