
def solution(absolutes, signs):
    answer = 123456789

    answer = 0

    for index in range(len(absolutes)) :
        if(signs[index]) :
            answer += absolutes[index]

        else :
            answer -= absolutes[index]

    return answer