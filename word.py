import random

#opens text file that has 400k words in which the computer will iterate through

class RandomWord:
    def __enter__(self):
        self.f = open("words.txt", "r")
        self.words = [word.strip().lower() for word in self.f if len(word.strip()) == 5 and word.strip().isalpha()]
        return random.choice(self.words)
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()




