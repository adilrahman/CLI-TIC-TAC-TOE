import random

class TicTacToe:
    def __init__(self):
        self.board = [] 
        self.X = False
        self.Y = False

    def startGame(self):
        if(random.randint(1,10) > 5):
            self.X = True
        else:
            self.Y = True
        self.create_a_board()
        self.display_board()
        self.play()
   
    def create_a_board(self):
        for i in range(9):
            self.board.append(" - ")
    
    def display_board(self):
        if self.X:
            print(f"Player X ")
        elif self.Y:
            print(f"Player Y")
        else:
            print("nothing")

        print("-----------------")
        for i in range(9):
            if i in (3,6,9):
                print("\n-----------------")
            print(self.board[i], end=" | ")
        print("\n-----------------")
    
    def play(self):
        while True:
            if self.X == True:
                self.X,self.Y = False,True
                move = str(input("move : "))
            else:
                self.X,self.Y = True,False
                move = str(input("move : "))




if __name__ == "__main__":
    t = TicTacToe()
    t.startGame()
