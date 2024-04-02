a = [
    [3, 1, 0, 4, 8, 0, 9, 2, 5],
    [5, 6, 0, 0, 0, 0, 0, 0, 7],
    [2, 4, 0, 7, 3, 5, 6, 8, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 9],
    [7, 0, 2, 8, 6, 0, 0, 0, 0],
    [0, 0, 4, 0, 5, 1, 2, 0, 0],
    [0, 0, 0, 0, 7, 8, 0, 9, 4],
    [4, 0, 0, 0, 0, 0, 8, 1, 0],
    [0, 0, 5, 1, 0, 0, 0, 0, 0]
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
    
    return False


def is_valid_movement(board, number, position):
    """ Check if the giving number can be add to the position"""
    print(f"TESTE {number} em {position}")
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

    # 1) Find the next place to fill
    place = find_empty_place(board)
    
    # If there is a place to fill, take the positions,  
    if place:
        row, col = place

    # IF SOLVED: otherwise the board is completed. Here is de END point
    else:
        print("No more places to fill. Game completed")
        return True
    
    # 2) Try all 9 numbers for this place
    for i in range (1, 10):
        
        # 3) Fill this place with the first available option
        if is_valid_movement(board, i, place):
            print(f"Add {i} in position {place}")
            board[row][col] = i

            # 4) Than do all the process again
                # Here is the secret: If call the function again and there is no more places to fill,
                # the function will return True and end it.
            if solve_sudoku(board):
                return True
            
            # 5) But if the next movement is impossible, set the place to ZERO, and continue to check other numbers
                # Here is the Backtrack! You tried to solve but there are no options, so go back one position e try other number
            print(f"SEM solução. Voltando 0 para {row,col}")
            board[row][col] = 0
    
    # 6) If you tired all 9 number for that position  
        # and there are NO possible number to put there,
        # so return FALSE and try other number in the LAST position
    return False



         
print_board(a)
solve_sudoku(a)
print_board(a)

            

