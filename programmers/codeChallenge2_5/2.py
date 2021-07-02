def solution(numbers):
    answer = []

    for number in numbers :

        num = '0' + bin(number)[2:]
        
        if num[-1] == '0' :
            answer.append(number+1)
        else :
            for i in range(len(num)-1, -1, -1) :
                if num[i] == '0' :
                    num = num[:i] + '10' + num[i+2:]
                    break
            
            answer.append(int('0b' + num,2))


    return answer

print(solution([2, 7]))