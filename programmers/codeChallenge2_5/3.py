def solution(s):
    answer = []

    for sen in s :
        answer.append(find(sen))


    return answer

def find(sen) :


    ret = ('1') * 50
    
    sen2 = sen[:sen.index('110')] + sen[sen.index('110')+3:]
        

    for i in range(len(sen2)) :

        temp = sen2[:i] + '110' + sen2[i:]
        print(temp)

        if(sen == temp) :
            return sen

        ret = min(int('0b' + find(temp), 2), int('0b' + ret, 2))

        ret = bin(ret)[2:]

    return ret


print(solution(["1110","100111100","0111111010"]))

# ["1101","100110110","0110110111"]