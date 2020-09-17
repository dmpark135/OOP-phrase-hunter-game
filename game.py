# Create your Game class logic in here.
import random
from phrase import Phrase

class Game:

    
    def __init__(self, missed = 0, phrases = [], active_phrase = None, guesses = []):
        self.missed = missed
        self.phrases = [Phrase('Hello world'),
            Phrase('there is no trying'),
            Phrase('May the force be with you'),
            Phrase('you have to see the matrix for yourself'),
            Phrase('life is like a box of chocolates')
            ]
        self.active_phrase = self.get_random_phrase()
        
        self.guesses = []
        
    def welcome(self):
        print("Welcome to the Thunderdome \n")
        
    def get_random_phrase(self):
        return random.choice(self.phrases)
   
    def start(self):
        self.welcome()
        print("Number missed: " + str(self.missed))
        print(self.active_phrase.display(self.guesses))
        user_guess = self.get_guess()
        self.guesses.append(user_guess)
       
        print(self.active_phrase.display(self.guesses))
        

    def get_guess(self):
        
        x = input('Enter a letter: ')
        return x
        
        
      

        
        
