import sys


def get_input(input_file):
    # make a list of inputs
    board = []
    for line in input_file:
        line = list(map(int, line.split()))
        board.append(line)
    return board


def find_zeros(board):
    # find 0's on table and put them on a list as tuple
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells


def check(board, row, col, num):
    # check current row for number
    for x in range(9):
        if board[row][x] == num:
            return False

    # check current column for number
    for x in range(9):
        if board[x][col] == num:
            return False

    # check current 3x3 subgrid for number
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def write_output(output_file, board, step, pos, i, j):
    output_file.writelines("-" * 18 + '\n')  # Dash "-" character printed out for 18 times

    output_file.writelines("Step {} - {} @ R{}C{}".format(step, pos, i, j) + '\n')
    ''' Step <SN>-<VAL>@ R<ROW>C<COL>
        <SN>: Number of current step.
        <VAL>: Value of the last solved cell.
        <ROW>: Row number of the last solved cell.
        <COL>: Column number of the last solved cell.'''

    output_file.writelines("-" * 18 + '\n')

    for row in board:
        if row == board[-1]:
            row_str = ' '.join(map(str, row))
            output_file.write(row_str + '\n')
            break
        row_str = ' '.join(map(str, row))
        output_file.write(row_str + '\n')


def solver(board, output_file):
    step = 1
    empty_cells = find_zeros(board)
    # Continue solving until there are no empty cells left
    while len(empty_cells) > 0:
        for i, j in empty_cells:
            if board[i][j] == 0:

                # List to store possible numbers for the current cell
                possibility = []

                for num in range(1, 10):
                    if check(board, i, j, num):
                        possibility.append(num)

                # If there is only one possibility, fill the cell
                if len(possibility) == 1:
                    board[i][j] = possibility[0]
                    write_output(output_file, board, step, possibility[0], i + 1, j + 1)
                    step = step + 1
                    empty_cells.remove((i, j))
                    empty_cells = find_zeros(board)
                    break  # when you fill a cell loop is start again


def main():
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")
    board = get_input(input_file)
    solver(board, output_file)
    output_file.writelines("-" * 18 + '\n')
    input_file.close()
    output_file.flush()
    output_file.close()


if __name__ == "__main__":
    main()



