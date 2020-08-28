#!/use/bin/python3

from Game import App
 
class TicTacToe(App):
    def __init__(self):
       super().__init__() 
       self.options ={
                        "1) Play with computer"    : lambda : print("Not Yet"),
                        "2) Play in same computer" : self.startGame,
                        "3) Play with different computer" : lambda : print("Not Yet") 
                      }

    def appStart(self):
        for i in self.options.keys():
            print(i)
        res = int(input("\n> "))
        self.options[list(self.options.keys())[res-1]]()

if __name__ == "__main__":
    t = TicTacToe()
    t.appStart()
