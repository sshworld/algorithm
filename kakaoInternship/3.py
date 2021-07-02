
import timeit

table = {0 : '무지', 1 : '콘', 2 : '어피치', 3 : '제이지', 4 : '프로도', 5 : '네오', 6 : '튜브', 7 : '라이언'}
dTable = {v:k for k, v in table.items()}

def solution(n, k, cmd):
    answer = ''

    stack = []
    ans = ['무지', '콘', '어피치', '제이지', '프로도', '네오', '튜브', '라이언']

    for s in cmd :
        if s == "C" :
            stack.append(ans[k])
            ans.remove(ans[k])
            if k >= len(ans) :
                k = len(ans) - 1
        if s == "Z" :
            top = stack.pop()
            key = dTable.get(top)
            ans.insert(key, table[key])
            if k >= key :
                k = k + 1
        if s[0] == "D" :
            k = k + int(s[2])
        if s[0] == "U" :
            k = k - int(s[2])
        
    for i in range(n) :
        if table[i] not in ans :
            answer += 'X'
        else :
            answer += 'O'
    return answer

start_time= timeit.default_timer()
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
end = timeit.default_timer()
print(end-start_time)