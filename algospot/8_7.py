
def findLevel(num) :

    # level 1
    if(len(set(num)) == 1) :
        return 1

    prev = num[0] - 1

    # level 2
    for val in num :
        if (val - prev != 1) :
            break
        
        prev = val
    else : 
        return 2

    prev = num[0] + 1

    for val in num :
        if (prev - val != 1) :
            break
        prev = val
    else :
        return 2

    # level 3
    twoNums = [num[0], num[1]]

    ok = False

    for val in num :
        if(twoNums[ok] != val) :
            break
        ok = not ok
    else :
        return 4

    #level 4
    seq = num[1] - num[0]
    prev = num[0] - seq

    for val in num :
        if(val != prev + seq) :
            break
        prev = val
    else :
        return 5

    return 10

def start(numbers, startNum, dp) :

    n = len(numbers)

    if(n == startNum) :
        return 0
    
    if (dp[startNum]) :
        return dp[startNum]

    
    ret = 99999

    for i in range(3, 6) :
        if (startNum + i <= n) :
            ret = min(ret, start(numbers, startNum + i, dp) + findLevel(numbers[startNum:startNum+i]))


    dp[startNum] = ret

    return dp[startNum]

def main() :

    c = int(input())
    ans=[0 for _ in range(c)]

    for i in range(c) :
        
        numbers = list(map(int, input()))

        dp = [0 for _ in range(len(numbers))]

        ans[i] = start(numbers, 0, dp)

    for q in ans :
        print(q)

main()