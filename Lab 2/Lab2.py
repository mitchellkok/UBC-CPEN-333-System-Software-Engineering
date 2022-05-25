# student name: Mitchell Kok
# student number: 44572246
import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()


    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """

        print("")
        print("   %s | %s | %s    0 | 1 | 2" % (self.board[0], self.board[1], self.board[2]))
        print("   --+---+--    --+---+--")
        print("   %s | %s | %s    3 | 4 | 5" % (self.board[3], self.board[4], self.board[5]))
        print("   --+---+--    --+---+--")
        print("   %s | %s | %s    6 | 7 | 8" % (self.board[6], self.board[7], self.board[8]))
        print("")


    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        while True:
            # loop until valid user input
            userinput = input("> Next move for X (state a valid cell num): ")

            try:
                userinteger = int(userinput)
                if userinteger > 8 or userinteger < 0 or self.board[userinteger] != ' ':
                    # reject invalid integer inputs or cells already populated
                    print("Must enter a valid cell number")
                else:
                    print("You chose cell %d" % userinteger)
                    self.board[userinteger] = 'X'
                    self.printBoard()
                    break
            except ValueError:
                # reject non-integer inputs
                print("Must be an integer")



    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        while True:
            # loop until valid computer-generated input
            computerinteger= random.randint(0, 8)
            if self.board[computerinteger] == ' ':
                print("Computer chose cell %d" % computerinteger)
                self.board[computerinteger] = 'O'
                self.printBoard()
                break


    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        # check rows
        for i in range(0, 7, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == who:
                return True
        
        # check columns
        for i in range(0, 3, 1):
            if self.board[i] == self.board[i+3] == self.board[i+6] == who:
                return True
        
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] == who:
            return True
        if self.board[2] == self.board[4] == self.board[6] == who:
            return True

        return False


    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        # check for winner
        if self.hasWon(who):
            if who == 'X':
                print("You won! Thanks for playing.")
            elif who == 'O':
                print("You lost! Thanks for playing.")
            return True
        
        # check for empty spaces
        for i in range(9):
            if self.board[i] == ' ':
                return False
        
        # return in case of draw
        print("A draw! Thanks for playing.")
        return True

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate