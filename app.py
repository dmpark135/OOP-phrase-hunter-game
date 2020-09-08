
from phrase import Phrase
from game import Game

def main():

    phrase = Phrase('Life is like a box of chocolates')
    game = Game()
    
    for phrase in game.phrases:
        print(phrase.phrase)
   

   
    
if __name__ =='__main__':
    
        main()


## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
