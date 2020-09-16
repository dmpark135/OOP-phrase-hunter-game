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
        user_guess = self.get_guess([])
        self.guesses.append(user_guess)
        my_str = ''
        for i in self.guesses:
          my_str = my_str + i
        print(my_str)
        print(self.active_phrase.display(self.guesses))
        
     '''   
    def start(self):
        self.welcome()
        print('numbered missed: ' + str(self.missed))  # print the number of missed
        print(self.active_phrase.display(self.guesses))
        user_guess = self.get_guess()  # a single char
        self.guesses.append(user_guess)  # append the char to the list of guesses

        my_str = ''
        for i in self.guesses:
          my_str = my_str + i
        print(my_str)
        print(self.active_phrase.display(self.guesses))    
            
       ''' 
    def get_guess(self):
        
        self.guesses = input('Enter a letter: ')
        print(self.guesses)
        
        
      

        
        
