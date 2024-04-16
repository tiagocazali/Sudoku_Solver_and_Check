# Sudoku Solver - with Backtracking

This Python script provides a Sudoku solver using a backtracking algorithm. 

Basically, the algorithm iterates through each empty space (designated by the number zero) one by one and fills it with the first valid number, then moves to the next space. If it encounters a space where no valid solution exists, the algorithm backtracks to the previous space and tries the next valid number. This process continues until the puzzle is completed.

## What is Sudoku
Sudoku is a popular puzzle game where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contain all of the digits from 1 to 9 without repetition.

## Usage

1) To use this solver, simply provide a 9x9 grid as a list of lists, where each inner list represents a row of the Sudoku board. 
- Empty cells should be represented by `0`. For example:

```python
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
```

2) Call the solve_sudoku function

    `solve_sudoku(a)`

3) Print the solved Sudoku board
   
    `print_board(a)`


## Main Functions

- `solve_sudoku(board)`

This function solves the Sudoku puzzle provided as `board`, using a backtracking algorithm.

- `print_board(board)`

Prints the Sudoku board in a readable format.


## Auxiliar Functions
- `find_empty_place(board)`

Returns the coordinates of the first empty cell (row, col) on the Sudoku board. If there are no empty cells, returns `False`.

- `is_valid_movement(board, number, position)`

Checks whether it's valid to place "number" at the specified "position" on the Sudoku board. Returns "True" if the move is valid, "False" otherwise.


## Acknowledgments
  

- Special thanks to [Tech With Tim](https://www.youtube.com/watch?v=lK4N8E6uNr4)
- Special thanks to [Inside Code](https://www.youtube.com/watch?v=eAFcj_2quWI)