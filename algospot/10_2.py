
def main() :
    
    c = int(input())

    ans = []

    for i in range(c) :

        n = int(input())

        warmTime = list(map(int, input().split()))

        eatTime = list(map(int, input().split()))

        lunch_boxes = sorted(zip(warmTime,eatTime), key = lambda x : (-x[1],x[0]))

        maxTime = 0
        warmTotal = 0

        for i, box in enumerate(lunch_boxes) :
            warmTotal += box[0]
            maxTime = max(maxTime, warmTotal + box[1])

        ans.append(maxTime)

    for answer in ans :
        print(answer)

main()