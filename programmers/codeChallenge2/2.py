def find(s, Queue) :
    for i in s: 
        if i == '(': Queue[0] += 1
        elif i == '[' : Queue[1] += 1
        elif i == '{' : Queue[2] += 1
        elif i == ')': Queue[0] -= 1
        elif i == ']' : Queue[1] -= 1
        elif i == '}' : Queue[2] -= 1

        if Queue[0] < 0 :
            return 0
        elif Queue[1] < 0 :
            return 0
        elif Queue[2] < 0 :
            return 0
    
    if sum(Queue) == 0 :
        return 1
    else :
        return 0
        


def solution(s):
    answer = 0

    for _ in range(len(s)) :
        left = s[:-1]
        right = s[-1:]

        s = right + left

        Queue = [0 for _ in range(3)]

        answer += find(s, Queue)

        Queue[0] = 0
        Queue[1] = 0
        Queue[2] = 0
    
    return answer


# Queue = []
# def find(s) :
#     for i in s: 
#         if i == '(': Queue.append('(')
#         elif i == '[' : Queue.append('[')
#         elif i == '{' : Queue.append('{')
#         else: 
#             try: Queue.pop() 
#             except: return 0
#         if len(Queue) == 0: return 1
#         else: return 0

# def solution(s):
#     answer = 0

    
    
#     for index in range(len(s)) :
#         left = s[:-index]
#         right = s[-index:]

#         s = right + left

#         answer += find(s)
    
#     Queue.clear

#     return answer