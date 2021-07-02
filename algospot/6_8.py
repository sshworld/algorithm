
switch = [
        [0,1,2],
        [3,7,9,11],
        [4,10,14,15],
        [0,4,5,6,7],
        [6,7,8,10,12],
        [0,2,14,15],
        [3,14,15],
        [4,5,7,14,15],
        [1,2,3,4,5],
        [3,4,5,9,13]
    ]

def push(now, num, clock) :
    
    for _ in range(num) :
        for i in switch[now] :
            clock[i] = (clock[i] + 1) % 4

    return clock

def find(clock, now) :

    if max(clock) == 0 :
        return 0

    if now == 10 :
        return float('inf')

    ret = float('inf')

    for i in range(4) :
        ret = min(ret, i + find(clock, now + 1))
        clock = push(now, 1, clock)

    return ret

def main() :

    c = int(input())

    ans = []

    for _ in range(c) :
        clock = list(map(int, input().split()))

        clock = [i/3%4 for i in clock]

        ans.append(find(clock, 0))

    for answer in ans :
        print(answer)

main()