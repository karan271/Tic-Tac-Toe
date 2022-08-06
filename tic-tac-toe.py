def is_full(board):
    for row in board:
        for cell in row:
            if not cell:
                return False

    return True


def check_win_row(x):
    win = True
    n = len(arr)


#rows
    for i in range(n):
        win = True
        for j in range(n):
            if arr[i][j] != x:
                win = False
                break
        if win:
            return win
    return win


def check_win_col(x):
    win = True
    n = len(arr)

    #columns
    for i in range(n):
        win = True
        for j in range(n):
            if arr[j][i] != x:
                win = False
                break
        if win:
            return win
    return win


def check_win_diagleft(x):
    win = False

    if arr[0][0] == arr[1][1] == arr[2][2] == x or arr[0][2] == arr[1][1] == arr[2][0] == x:
        win = True

    return win


if __name__ == "__main__":
    rows, cols = (3, 3)

    arr = [[0 for _ in range(3)] for _ in range(3)]
    for row in arr:
        for cell in row:
            print(' _' if row else cell , end='')
        print()

    while not is_full(arr):
        p1 = input("Player 1: Enter the location -> ")
        pos = list(map(int,p1.split(',')))
        arr[pos[0]][pos[1]] = 'x'
        for row in arr:
            for cell in row:
                print(' _' if not cell else f' {cell}' , end='')
            print()

        print(check_win_row('x'))
        print(check_win_col('x'))
        print(check_win_diagleft('x'))
        if check_win_row('x') or check_win_col('x') or check_win_diagleft('x'):
            print('Its a win for Player 1')
            break

        p2 = input("Player 2: Enter the location -> ")
        pos = list(map(int, p2.split(',')))
        arr[pos[0]][pos[1]] = 'o'
        for row in arr:
            for cell in row:
                print(' _' if not cell else f' {cell}' , end='')
            print()

        if check_win_row('o') or check_win_col('o') or check_win_diagleft('o'):
            print('Its a win for Player 2')
            break