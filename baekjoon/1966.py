import sys

n = int(sys.stdin.readline())

answer = []
ms = []
prioritys = []

for _ in range(n) :
    doc, m2 = map(int, sys.stdin.readline().split())
    ms.append(m2)
    prioritys.append(list(map(int, sys.stdin.readline().split())))

for i in range(n) :
    count = 1
    m = ms[i]
    priority = prioritys[i]

    while True :

        if priority[0] == max(priority) :
            if m == 0 :
                answer.append(count)
                break
            else :
                del priority[0]
                count += 1
                m -= 1
        else :
            temp = priority[0]
            del priority[0]
            priority.append(temp)
            
            if m == 0 :
                m = len(priority) - 1
            else :
                m -= 1
    
s = ''

for i in answer:
        s += (str(i) + '\n')
print(s)