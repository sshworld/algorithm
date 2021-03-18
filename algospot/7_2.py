
def find(tree, index) :

    if(index >= len(tree)) :
        return ""

    charPoint = tree[index]

    if(charPoint == 'w') :
        return 'w'

    if(charPoint == 'b') :
        return 'b' 
    
    index += 1
    lt = find(tree, index)

    index += len(lt)
    rt = find(tree, index)

    index += len(rt)
    lb = find(tree, index)

    index += len(lb)
    rb = find(tree, index)

    return "x" + lb + rb + lt + rt



def main() :

    c = int(input())

    ans = []

    for _ in range(c) :

        tree = list(map(str, input()))

        ans.append(find(tree, 0))

    print(ans)

main()