

class Phrase:
    def __init__(self, phrase):
               
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        for i in range(len(self.phrase)):
            if self.phrase[i] in guesses:
                print(f"{self.phrase[i]} ", end = "")
            else:
                print('_', end = "")


MY_PHRASE = Phrase('Hi David')
# print(MY_PHRASE.phrase)
print(MY_PHRASE.display('dv'))   
        
    
        
        