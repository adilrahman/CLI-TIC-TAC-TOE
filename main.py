
class TicTacToe:
    def __init__(self):
        self.board = [] 
        self.X = False
        self.Y = False
    
    def create_a_board(self):
        for i in range(9):
            self.board.append(" - ")
    
    def display_board(self):
        print(f"Player : X")
        print("-----------------")
        for i in range(9):
            if i in (3,6,9):
                print("\n-----------------")
            print(self.board[i], end=" | ")
        print("\n-----------------")
                
if __name__ == "__main__":
    t = TicTacToe()
    t.create_a_board()
    t.display_board()
