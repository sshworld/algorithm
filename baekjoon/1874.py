import sys

def pop() : 
    global count
    del stack[-1]
    answer.append('-')

def push() :
    global count

    stack.append(count)
    count += 1
    answer.append('+')

n = int(sys.stdin.readline())

stack = []
count = 1
answer = []

k = []

for _ in range(n) :
    temp = int(sys.stdin.readline())
    k.append(temp)

for i in range(n) :

    if len(stack) == 0 :
        push()

    while True :
        if k[i] == stack[-1] :
            pop()
            break
        elif k[i] > stack[-1] :
            push()
        else :
            answer = 'NO'
            break

    if answer == 'NO' :
        break

s = ""
if answer == 'NO' :
    s = 'NO'
else :
    for i in answer:
        s += (str(i) + '\n')
print(s)