def solution(left, right):
    answer = 0

    for num in range(left, right + 1) :
        
        ret = []
        ret.append(num)

        for i in range(1, int(num/2) + 1) :
            if num % i == 0 :
                ret.append(i)
                
        if len(ret) % 2 == 0 :
            answer = answer + num
        else :
            answer = answer - num

    

    return answer