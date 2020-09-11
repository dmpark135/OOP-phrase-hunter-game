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
        self.active_phrase = get_random_phrase
        #can't test this
        self.guesses = [" "]
        
    def get_random_phrase(self):
        return random.choice(self.phrases))
      

        
        
