import random
"""This game plays hangman with the user."""
class Hangman:

    def __init__(self):
        self.hidden_word = self.find_word()
        self.blank_string = "-" * len(self.hidden_word)
        self.lives = 6
        
        #For debugging only ;)
        print self.hidden_word
        print self.blank_string

    def process_guess(self, guess):
      if guess!=self.hidden_word:
	return True
      else:
	return False
        #your code here (this should be called from play)
        
    def find_word(self):
        #This method is complete
        dictionary = open('/usr/share/dict/words','r')
        words = list(dictionary)
        return random.choice(words).lower().strip()
        
    def draw_hangman(self, lives):
        if lives == 6:
            print "=========\n ||     |\n ||\n ||\n ||\n ||\n/  \\"
        elif lives == 5: 
            print "=========\n ||     |\n ||     O\n ||\n ||\n ||\n/  \\"
        elif lives == 4:
            print "=========\n ||     |\n ||     O\n ||     |\n ||\n ||\n/  \\"
        elif lives == 3:
            print "=========\n ||     |\n ||    \O\n ||     |\n ||\n ||\n/  \\"
        elif lives == 2: 
            print "=========\n ||     |\n ||    \O/\n ||     |\n ||\n ||\n/  \\"
        elif lives == 1: 
            print "=========\n ||     |\n ||    \O/\n ||     |\n ||    /\n ||\n/  \\"
        elif lives == 0:
            print "=========\n ||     |\n ||     O \n ||    /|\\\n ||    / \\\n ||\n/  \\"
            
    def won_game(self):
      if self.lives!=0:
	print("You WON!")
      else:
	print("You LOSE!")
      #Your code here (this should be called from play)
        
    def play(self):
      guess = raw_input("I'm thiking of a word, can you guess what it is? ")
      while self.process_guess(guess) & (self.lives>0):
	guess = raw_input("Wrong! Guess again! ")
	self.lives-=1
	self.draw_hangman(self.lives)
      self.won_game()
       #Your code here
        
    
if __name__ == "__main__":
    game = Hangman()
    game.play()