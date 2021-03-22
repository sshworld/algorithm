
import sys
rl = lambda : sys.stdin.readline()

def findIS(dp, s, index) :

    isLists = []

    for i in range(1, index) :

        max = 1
        isList = []
        for j in range(i) :
            if(s[i] > s[j] and max <= dp[j]) :
                max += 1
                isList.append(s[j])
        isList.append(s[i])
        isLists.append(isList)
        dp[i] = max

    isList.append(s[0])

    return isLists


def makeLIS(aList, bList) :

    length = []

    for i in range(len(aList)) :
        
        for j in range(len(bList)) :

            c1 = aList[i] + bList[j]

            c1 = list(set(c1))

            length.append(len(c1))

    return max(length)

def main() :
    
    c = int(rl())

    ans = []

    for _ in range(c) :

        n, m = map(int, rl().split())

        ndp = [1 for _ in range(n)]
        mdp = [1 for _ in range(m)]

        a = list(map(int, rl().split()))
        b = list(map(int, rl().split()))

        ndp = findIS(ndp, a, n)
        mdp = findIS(mdp, b, m)

        ans.append(makeLIS(ndp, mdp))
    
    for i in ans :
        print(i)

    sys.exit(1)

main()

