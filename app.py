
from game import Game



def main():
    game = Game()

game.welcome()

    
def print_phrase(x):
    print(f"The phrase is:{x.phrase}")
   
   
game = Game()

print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())    
     
print(game.active_phrase.phrase)

    
if __name__ =='__main__':
    
        main()


## 