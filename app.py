

def getDiagonals(matrix, x, y):
    width, height = len(matrix[0]), len(matrix)
    size = max(width, height)
    valid_x, valid_y = range(width), range(height)
    diag1 = [matrix[i][i-x+y] for i in range(size) if i-x+y in valid_y]
    diag2 = [matrix[i][x+y-i] for i in range(size) if x+y-i in valid_y]
    return (diag1, diag2)


def clean_list(lst, reverse=False):
    new_list = []
    obstacles = False
    iter = range(lst.index(1), -1, -
                 1) if reverse else range(lst.index(1), len(lst))
    for idx in iter:
        item = lst[idx]
        print(item)
        if item == 0 and not obstacles:
            new_list.append(item)
        elif item == 2:
            obstacles = True
    return new_list


def queensAttack(n, k, r_q, c_q, obstacles):
    """
    - int n: the number of rows and columns in the board
    - nt k: the number of obstacles on the board
    - int r_q: the row number of the queen's position
    - int c_q: the column number of the queen's position
    - int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle

    Matrix values:
        2 = obstacle
        1 = current queen position
        0 = free position
    """

    board = [[0]*n for i in range(n)]
    row_queen_position = r_q - 1
    column_queen_position = c_q - 1

    board[row_queen_position][column_queen_position] = 1

    # Set position of obstacles
    for obstacle in obstacles:
        board[obstacle[0] - 1][obstacle[1] - 1] = 2

    diagonal_movements = 0
    row_movements = 0
    column_movements = 0

    for row in board:
        for item in row:
            if item == 1:
                diagonals = getDiagonals(
                    board, row_queen_position, column_queen_position)
                column = [r[column_queen_position] for r in board]

                row_clean = clean_list(row) + clean_list(row, reverse=True)
                column_clean = clean_list(
                    column) + clean_list(column, reverse=True)

                row_movements = len(row_clean)
                column_movements = len(column_clean)

                for diagonal in diagonals:
                    diagonal_clean = clean_list(
                        diagonal)
                    diagonal_clean_reverse = clean_list(
                        diagonal, reverse=True)

                    diagonal_movements += len(
                        diagonal_clean) + len(diagonal_clean_reverse)

                break
        else:
            continue
        break

    total_movements = row_movements + column_movements + diagonal_movements
    return total_movements
