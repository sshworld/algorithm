from itertools import combinations

def findFriend(n, pairs, taken) :

    #짝 완성 여부
    if(sum(taken) == n) :
        return 1

    # 가장 앞에 있는 사람 중 짝이 안지어져 있는 사람 찾기
    for i in range(n) :
        if (not taken[i]) :
            break

    # 카운트 초기화
    count = 0

    # 짝이 안정해져있고, 서로 짝인지 여부 검사 후 초기화
    for j in range(n) :
        if(not taken[j] and pairs[i][j]) :
            taken[i] = taken[j] = True
            count += findFriend(n, pairs, taken)
            taken[i] = taken[j] = False
    
    return count

def main() :
    c = int(input())

    count = [0 for _ in range(c)]

    for index in range(c) :
        
        n, m = map(int, input().split())

        # 짝 완성 여부를 위한 변수
        taken = [False] * n
        
        # 서로의 친구를 나타내주는 행렬
        pairs = [[0] * n for _ in range(n)]

        # 친구 번호
        friend = list(map(int, input().split()))

        # 친구 여부에 대한 행렬 값 입력
        for i in range(m) :
            p = friend[2 * i]
            q = friend[2 * i + 1]

            pairs[p][q] = pairs[q][p] = 1
        
        count[index] = findFriend(n, pairs, taken)

    print(count)

main()
               
