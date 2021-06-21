
def solve(dp, n) :

    if(dp[n]) :
    

def main() :
    
    c = int(input())

    mod = 1000000007

    ans = []



    for i in range(c) :
        n = int(input())
        dp = [-1 for _ in range(n)]

        dp[0] = 1
        dp[1] = 2

        ans[i] = solve(dp, n)

    print(dp)

main()


        
