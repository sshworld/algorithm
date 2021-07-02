
def solution(a, edges):
    

    if sum(a) :
        return -1

    tree = [list() for i in range(len(a))]

    visited = [0] * len(a)

    for i in range(len(edges)) :
        tree[edges[i][0]].append(edges[i][1])
        tree[edges[i][1]].append(edges[i][0])

    global answer
    answer = 0
        
    def find(node) :
    
        global answer
        if visited[node] :
            return 0

        visited[node] = 1

        for i in range(len(tree[node])) :
            a[node] += find(tree[node][i])
        
        son = a[node]
        a[node] = 0
        answer += abs(son)
        return son

    find(0)
    if not a[0] :
        return answer

    return -1