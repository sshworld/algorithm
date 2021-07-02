
def man(x, y) :

    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def find(place) :

    p = []

    for i in range(len(place)) :
        for j in range(len(place[i])) :
            if place[i][j] == 'P' :
                p.append([i, j])
    print(p)
    if len(p) == 0 :
        return 1

    for i in range(len(p)-1) :
        for j in range(i+1, len(p)) :
            distance = man(p[i], p[j])

            if distance == 1 :
                print("헷")
                return 0
            if distance <= 2 :
                if p[i][0] > p[j][0] :
                    if place[p[j][0]+1][p[j][1]] != 'X' or place[p[j][0]][p[j][1]+1] != 'X':
                        print('ㄱ')
                        return 0
                else :
                    if p[i][0] != p[j][0] and p[j][0] >= 1 and place[p[j][0]-1][p[j][1]] != 'X' : 
                        print('ㄴ')
                        return 0
                    if p[i][1] != p[j][1] and p[j][1] >= 1 and place[p[j][0]][p[j][1]-1] != 'X' : 
                        print('i')
                        return 0
                # if abs(p[j][0] - p[i][0]) == 1 and abs(p[j][1] - p[i][1]) == 1 :
                    

    return 1


def solution(places):
    answer = []
    
    for place in places :

        answer.append(find(place))
        
    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))