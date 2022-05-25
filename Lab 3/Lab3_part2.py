# student name: Mitchell Kok
# student number: 44572246

import multiprocessing

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    
    checklist = [0,0,0,0,0,0,0,0,0] # initialize checklist for numbers in column
    for row in range(9):
        # iterate through rows
        number = puzzle[row][column] - 1
        if checklist[number] == 1:
            # number already exists
            print("Column %d not valid" % column)
            return
        else:
            # mark checklist for number
            checklist[number] = 1
    print("Column %d valid" % column)
  

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """

    checklist = [0,0,0,0,0,0,0,0,0] # initialize checklist for numbers in row
    for col in range(9): # iterate through columns
        number = puzzle[row][col] - 1
        if checklist[number] == 1: # number already exists
            print("Row %d not valid" % row)
            return
        else:
            checklist[number] = 1 # mark checklist for number
    print("Row %d valid" % row)


def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """

    checklist = [0,0,0,0,0,0,0,0,0] # initialize checklist for numbers in subgrid
    row_offset = 3 * (subgrid // 3) # top row of subgrid
    col_offset = 3 * (subgrid % 3)  # left column of subgrid

    for row in range(row_offset, row_offset + 3, 1): # iterate through rows
        for col in range(col_offset, col_offset + 3, 1): # iterate through columns
            number = puzzle[row][col] - 1
            if checklist[number] == 1: # number already exists
                print("Subgrid %d not valid" % subgrid)
                return
            else:
                checklist[number] = 1 # mark checklist for number
    print("Subgrid %d valid" % subgrid)


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5]
            ]
    
    testcase = test1   #modify here for other testcases
    SIZE = 9

    p_list = [] # initialize empty list for processes
    for col in range(SIZE):  #checking all columns
        p_list.append(multiprocessing.Process(target=checkColumn, args=(testcase, col, )))
    for row in range(SIZE):  #checking all rows
        p_list.append(multiprocessing.Process(target=checkRow, args=(testcase, row, )))
    for subgrid in range(SIZE):   #checking all subgrids
        p_list.append(multiprocessing.Process(target=checkSubgrid, args=(testcase, subgrid, )))

    for process in range(len(p_list)): # start all processes
        p_list[process].start()
    for process in range(len(p_list)): # join all processes
        p_list[process].join()