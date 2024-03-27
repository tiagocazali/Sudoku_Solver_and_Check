a = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(board):
    """Print the Board in Sudoku Format"""

    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-------------------------------")
        
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end='')
            
            if col == 8:
                print(board[row][col], end='\n')

            else:
                print(str(board[row][col]) + " ", end=' ')
        

def find_empty_place(board):
    """Return the first empty place in the board - (Row, Col)"""

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)


def is_valid_movement(board, number, position):
    """ Check if the giving number can be add to the position"""

    row, col = position

    #check the Row
    for i in range(9):
        if board[row][i] == number and col != i:
            print('Row Error')
            return False
        
    #check the Colum
    for i in range(9):
        if board[i][col] == number and row != i:
            print("Colum error")
            return False
    
    #check the quadrant:
    box_x = row//3
    box_y = col//3

    for i in range(box_x*3, box_x*3+3):
        for j in range(box_y*3, box_y*3+3):
            if board[i][j] == number:
                print("Box Error")
                return False


    return True
    

def solve_sudoku(board):
    

         
print_board(a)
            

