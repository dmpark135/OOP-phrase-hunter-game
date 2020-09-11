
from game import Game



def main():
    game = Game()
    
def print_phrase(x):
    print(f"The phrase is:{x.phrase}")
    #doen't work. why is the class behind vs game front
   
game = Game()
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())    
     
print(game.active_phrase)
print(game.active_phrase.phrase)

    
if __name__ =='__main__':
    
        main()


## 