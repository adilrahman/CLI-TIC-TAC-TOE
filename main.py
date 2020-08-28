import random
import os

class TicTacToe:
    def __init__(self):
        self.board = [] 
        self.X = False
        self.Y = False
        self.gameOver = False

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
        os.system("clear")
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
        while self.gameOver != True:
            print("\n")
            if self.X == True:
                
                player = " X "
                self.X,self.Y = False,True
            
            else:
                player = " Y " 
                self.X,self.Y = True,False
            self.move(player) 
    
    def move(self,player):
            move = str(input(f"({player}): move :- "))
            if move == 'quit' or move == 'exit':
                self.gameOver = True
                exit(0)
            try:
                move = int(move)
                move -= 1
                self.onBoardChange(move,player)
            except ValueError:
                print("Enter Number !")
                self.move(player)

    def isDraw(self):
        for i in self.board:
            if i  == " - ":
                return
        self.gameOver = True
        print("\n-------------DRAW-------------")
        self.replay()
    
    def onBoardChange(self,move,player):
        if move > 8 or move < 0 or self.board[move] != " - ":
             print("Not Possible !")
             self.move(player)
        else:
                self.board[move] = player
                self.display_board()
                self.winner(player)
                self.isDraw()     
                
    def winner(self,player):
         winningCombo = [[0,1,2],
                         [3,4,5],
                         [6,7,8],
                         [0,4,8],
                         [2,4,6],
                         [0,3,6],
                         [1,4,7],
                         [2,5,8]]
         for i in winningCombo:
             count = 0
             for j in i:
                 if self.board[j] != player:
                     break
                 else:
                    count += 1
                    if count == 3:
                        print(f"\n++++++++++++++ {player} - WIN  ++++++++++++++")
                        self.gameOver = True
                        self.replay()
    def replay(self):
        res = input("\nReplay (y/n) : ")
        if res == 'y':
            self.board.clear()
            os.system("clear")
            self.X,self.Y,self.gameOver = False,False,False
            self.startGame()
        elif res == 'n' :
            exit(0)
        else:
            print("y = Yes \nn = No")
            self.replay()
        
             
        

if __name__ == "__main__":
    t = TicTacToe()
    t.startGame()
