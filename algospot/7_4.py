
def main() :

    c = int(input())

    for _ in range(c) :

        n = int(input())

        woods = list(map, int(input().split()))

        woods.append(0)

        woodstack = []

        result = 0

        length = 0

        for j in range(n + 1) :
            while woodstack and woods[woodstack[-1]] >= woods[j] :
                position = woodstack[-1]
                del woodstack[-1]
                if not woodstack :
                    length = j
                else :
                    length = j - woodstack[-1] - 1
                area = length * woods[position]
                result = max(result, area)
            woodstack.append(j)
        print(result)

main()


# #fence
# import sys
 
 
# case = int(sys.stdin.readline())
# for i in range(case):
#     fencenum = int(sys.stdin.readline())  # 판자 수
#     fences = list(map(int, sys.stdin.readline().split()))  # 판자 높이
#     fences.append(0)  # 스택의 마지막 요소까지 처리해 줘야 하므로 넣음
#     fencestack = []  # 스택 역할을 할 리스트
#     result = 0
#     length = 0  # 너비
#     for j in range(fencenum+1):
#         while fencestack and fences[fencestack[-1]] >= fences[j]:  # 스택이 비지 않고, 스택에 저장된 위치의 높이가 현재 높이보다 크다면
#             position = fencestack[-1]  # 스택의 마지막 요소
#             del fencestack[-1]
#             if not fencestack:  # 스택이 비었다면
#                 length = j
#             else:  # 안 비었다면
#                 length = j - fencestack[-1] - 1
#             area = length * fences[position]  # 너비*높이
#             result = max(result, area)  # 최대값을 구한다
#         fencestack.append(j)
#     print(result)  # 출력