import sys

type = [[[0, 0], [1, 0], [0, 1]],
            [[0, 0], [-1, 0], [0, -1]],
            [[0, 0], [0, 1], [-1, 0]],
            [[0, 0], [0, -1], [1, 0]]]

dx = [[0, 1, 1], [0, 1, 0], [0, 1, 1], [0, 0, 1]]
dy = [[0, 0, -1], [0, 0, 1], [0, 0, 1], [0, 1, 1]]

# def findEmpty(board, x, y, index, status) :

    

#     ok = True

#     for i in range(3) :
#         bx = dx[index][i] + x
#         by = dy[index][i] + y
#         # bx = type[index][i][0] + x
#         # by = type[index][i][1] + y

#         if(bx < 0 or by < 0 or by >= len(board) or bx >= len(board[0])) :
#             ok = False

#         if(status and not ok) :
#             board[bx][by] = status
        
#         if(not status) :
#             board[bx][by] = status

#     return ok


def paint(board) :

    x = -1
    y = -1

    for col in range(len(board)) :
        for row in range(len(board[0])) :
            if(not board[col][row]) :
                x = col
                y = row
                break
        if(not y == -1) :
            break
        

    if (y == -1) :
        return 1
    
    count = 0

    for index in range(4) :

        ok = True

        for i in range(3) :
            bx = dx[index][i] + x
            by = dy[index][i] + y
            # bx = type[index][i][0] + x
            # by = type[index][i][1] + y

            if(not (bx < 0 or by < 0 or by >= len(board) or bx >= len(board[0]) or not board[bx][by])) :
                board[bx][by] = True
            else :
                ok = False

        if(not ok) :
            for i in range(3) :
                bx = dx[index][i] + x
                by = dy[index][i] + y
                if(not (bx < 0 or by < 0 or by >= len(board) or bx >= len(board[0]) or not board[bx][by])) :
                    board[bx][by] = False
        else :
            count += paint(board)        

    return count


def main() :

    sys.setrecursionlimit(10000)

    c = int(input())

    for _ in range(c) :
        
        h, w = map(int, input().split())

        board = [list(map(str, input())) for _ in range(h)]

        print(board)

        board = [[True if value=='#' else False for value in data] for data in board]

        print(board)

        print(paint(board))

main()