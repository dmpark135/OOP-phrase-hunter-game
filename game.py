# Create your Game class logic in here.
class Game:
    def __init__(self, missed = 0, phrases = [], active_phrase = None, guesses = []):
        self.missed = missed
        self.phrases = phrases
        self.active_phrase = active_phrase
        self.guesses = [" "]
        
        phrase = [
            'hello world',
            'there is no trying',
            'may the force be with you',
            'you have to see the matrix for yourself',
            'life is like a box of chocolates'
            ]
   
    
        
        
