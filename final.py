from dict import *
import random
REALDICTONARY = Dictionary
class HBoard:
    """A data type representing the game hangman with a text/terminal based game."""
    def __init__(self):
        # self.word = word
        self.guess = []
        self.wrongGuess = 0
        self.score1 = 0
        self.score2 = 0
        self.p1Wins = False
        self.p2Wins = False
        self.word = ''
        self.livesLeft = 0
        self.data = len(self.word)*'_'
        self.remainingVowels =  ['a', 'e', 'i', 'o', 'u']
        self.restOfAlph = ['b', 'c', 'f', 'g' , 'j', 'k', 'l', 'm', 'p', 'q', 'v', 'x', 'y', 'z','t', 'n', 's', 'h', 'r', 'd', 'w','a', 'e', 'i', 'o', 'u']
        self.possibleWords = REALDICTONARY 
        # self.data = len(word)*"_"

    def __repr__(self):
        """Construct the empty text-based board based on given word."""
        print()
        print(15*"_")
        print("|      |\n" + "|      |")
        print(3*"|\n"+"|")
        print(20*"─")

        return self.data
    
    def reset(self):
        self.guess = []
        self.wrongGuess = 0
        # self.score1 = 0
        # self.score2 = 0
        self.word = ''
        self.livesLeft = 0
        self.data = len(self.word)*'_'
        self.remainingVowels =  ['a', 'e', 'i', 'o', 'u']
        self.restOfAlph = ['b', 'c', 'f', 'g' , 'j', 'k', 'l', 'm', 'p', 'q', 'v', 'x', 'y', 'z','t', 'n', 's', 'h', 'r', 'd', 'w','a', 'e', 'i', 'o', 'u']
        self.possibleWords = REALDICTONARY 
        self.False1 = False
        self.False2 = False

    def addGuess(self, c):
        """This method returns the player's guess in the correct index."""
        if c in self.word:
            print(self.data)
            amountofTimes = self.word.count(c)
            for x in range(amountofTimes):
                cIndex = self.word.index(c)
                self.data = replace(self.data, cIndex, c)
                self.word = replace(self.word, cIndex, '1')
            for x in range(amountofTimes):
                cIndex = self.word.index('1')
                self.word = replace(self.word, cIndex, c)

            self.bodyPart()
            print("Correct!")

        else:
            self.wrongGuess += 1
            self.bodyPart()
            self.livesLeft -= 1
            print("Wrong guess!")
            
        self.guess += c
        print(self.data)
        print()
        print("Lives left: " + str(self.livesLeft))
        print("Player's Guesses: "+ str(self.guess))
        return self.data
    
    def allowsGuess(self, c):
        """This method checks if the character input is one of the 26 characters and if it is lowercase, or if it has already been guessed."""
        # converts the letter into lowercase if it isn't already
        c = c.lower()
        if c == '' or len(c) > 1:
            return False
        elif (ord(c) >= 97) and (ord(c) <= 122):
            if c in self.guess:
                return False
            else:
                return True
        else:
            return False

    def scoreBoard(self):
        """This method retunrs the respective scores of each player."""



    # determines which body part to draw depending on the number of guess
    def bodyPart(self):
        """This method prints the visual lives of hangman based on how many guesses the player guessed wrong."""
        if self.wrongGuess == 1:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print("|      O\n" + 2*"|\n"+"|")
            print(20*"─")
            print()
        if self.wrongGuess == 2:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print("|      O\n" + "|      |" + 2*"\n|")
            print(20*"─")
            print()
        if self.wrongGuess == 3:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print("|      O\n" + "|     /|" + 2*"\n|")
            print(20*"─")
            print()
        if self.wrongGuess == 4:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print("|      O\n" + "|     /|\\" + 2*"\n|")
            print(20*"─")
            print()
        if self.wrongGuess == 5:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print("|      O\n" + "|     /|\\" + "\n|     /" + "\n|")
            print(20*"─")
            print()
        if self.wrongGuess == 6:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print("|      O\n" + "|     /|\\" + "\n|     / \\" + "\n|")
            print(20*"─")
            print()
        # if self.wrongGuess == 7:
        #     print()
        #     print(15*"_")
        #     print("|      |\n" + "|      |")
        #     print(3*"|\n"+"|")
        #     print(20*"─")
        #     print()
        if self.wrongGuess == 0:
            print()
            print(15*"_")
            print("|      |\n" + "|      |")
            print(3*"|\n"+"|")
            print(20*"─")
            print()
    
    def win(self):
        """This method returns true if the player wins and false otherwise."""
        if self.data == self.word:
            return True

    def lose(self):
        """This method returns true if the player loses and false otherwise."""
        if self.livesLeft == 0:
            return True
    
    def aiWord(self):
        """This method returns the word and its (corresponding data(length of the word)) the ai picks for the player to guess."""
        self.word = random.choice(REALDICTONARY)
        self.data = len(self.word)*"_"
        self.livesLeft = 6
    
    def aiGuessVowel(self):
        """This method returns the vowel the AI guesses"""
        randomVowel = random.choice(self.remainingVowels)
        self.remainingVowels.remove(randomVowel) # im not saying thank u
        if randomVowel in self.restOfAlph:
            self.restOfAlph.remove(randomVowel)

        if randomVowel in self.word:
            self.possibleWords = sortList(self.word.index(randomVowel),randomVowel, self.possibleWords)
            # self.guessFilter()
            return randomVowel, True
        return randomVowel, False
        

    def aiGuessLetters(self):
        """This method returns the letters the AI guesses."""      
        randomLetter = random.choice(self.restOfAlph)
        self.restOfAlph.remove(randomLetter)
        if randomLetter in self.word:
            self.possibleWords = sortList(self.word.index(randomLetter), randomLetter, self.possibleWords)
        return randomLetter



    def human(self, player):
        """This method runs one game with one player"""
        word = str(input("Player " + str(player) + " Word: "))
        self.word = word
        self.data = len(word)*"_"
        self.livesLeft = 6
        if player == 1:
            player2 = 2
        if player == 2:
            player2 = 1

        print(self)
        print()

        while True:
            guess = str(input("Player\'s " + str(player2) + " guess: "))
            while self.allowsGuess(guess) == False:
                guess = str(input("Invalid input, guess again: "))
        
            self.addGuess(guess)
            print()
            if self.win() == True:
                print("Player "+ str(player2) + " win!")
                if player == 1:
                    self.score2 += 1
                    if self.score2 >= 3:
                        self.p2Wins = True
                        return
                else:
                    self.score1 += 1

                    if self.score1 >= 3:
                        self.p2Wins = True
                        return
                        
                break

            if self.lose() == True:
                print("The word was " + self.word)
                print("You ran out of lives, player " + str(player) + " wins!")

                if player == 1:
                    self.score1 += 1
                    if self.score1 >= 3:
                        self.p1Wins = True
                        return
                else:
                    self.score2 +=1
                    if self.score2 >= 3:
                        self.p2Wins = True
                        return

                break
        
        self.reset()

    def hostGameHuman(self):
        """This method hosts game where the word to guess is human-inputted"""
        while (True):
            self.human(1)
            print(f"player one score is {self.score1}")
            print(f"player two score is {self.score2}")
            if self.p2Wins:
                print("Player 2 WON!")
                break
            if self.p1Wins:
                print("Player 1 WON")
                break
            self.human(2)
            print(f"player 1 score is {self.score1}")
            print(f"player 2 score is {self.score2}")
            if self.p2Wins:
                print("Player 2 WON!")
                break
            if self.p1Wins:
                print("Player 1 WON")
                break

        
    def humanGuess(self):
        """This method hosts a game where the word to guess is given by an AI."""
        self.aiWord()
        print(self)
        print()
        # infinite loop until win or lose
        while True:
            # starts by taking the player's guess for the word 
            guess = str(input("Player\'s guess: "))
            while self.allowsGuess(guess) == False:
                guess = str(input("Invalid input, guess again: "))
            
            self.addGuess(guess)
            # print(self)
            
            if self.win() == True:
                print("You win!")
                self.score2 += 1
                break

            if self.lose() == True:
                print("The word was " + self.word)
                print("You ran out of lives, you lost!")
                self.score1 += 1
                break

    def hostgameAIHuman(self):
        """This method hosts AI vs human game until one of them reaches a score of 3."""
        AIscore = self.score1
        humanscore = self.score2
        while True:
            self.humanGuess()
            print("Human score: " + str(self.score2))
            print("AI score: " + str(self.score1))
            if self.score2 >= 3:
                self.p2Wins == True
                return
            if self.score1 >= 3:
                self.p1Wins == True
                return
            

            self.reset()
            self.AIGuessHumanWord()
            print("Human score: " + str(self.score2))
            print("AI score: " + str(self.score1))
            if self.score1 >= 3:
                self.p1Wins == True
                return 
            if self.score2 >= 3:
                self.p2Wins == True
                return
            self.reset()
        
    
    def AIGuessHumanWord(self):
        """This methods returns the guesses of the AI based on the human word."""
        word = str(input("Player's word: "))

        while word in Dictionary == False:
            self.word = word
        else:
            word = str(input("Please choose a word in the dictionary for the AI to guess: "))

        self.word = word
        self.data = len(word)*"_"
        self.livesLeft =6
        print(self)
        print()
        
        self.possibleWords = sortByLength(len(self.word), REALDICTONARY)
        guess, rightGuess = self.aiGuessVowel()
        self.addGuess(guess)

        while (rightGuess != True) and (self.remainingVowels != []):
            guess, rightGuess = self.aiGuessVowel()
            self.addGuess(guess)

        while True:
            guess = self.aiGuessLetters()
            self.addGuess(guess)

            if self.win() == True:
                print("AI 1 wins!")
                self.score1 += 1
                return
    
            if self.lose() == True:
                print("The word was " + self.word)
                print("Human wins!")
                self.score2 += 1
                return

    def AIvsAI(self, AI):
        """This methods hosts an AI vs AI game."""
        self.reset()
        self.aiWord()

        print(self)
        print()


        
        self.possibleWords = sortByLength(len(self.word), REALDICTONARY)
        guess, rightGuess = self.aiGuessVowel()
        self.addGuess(guess)

        while (rightGuess != True) and (self.remainingVowels != []):
            guess, rightGuess = self.aiGuessVowel()
            self.addGuess(guess)
        while True:
            guess = self.aiGuessLetters()
            self.addGuess(guess)

            if self.win() == True:
                print(f"AI{AI} wins!")
                if AI==2:
                    self.score2+=1
                else:
                    self.score1 += 1
                break
    
            if self.lose() == True:
                print("The word was " + self.word)
                print(f"AI{AI} Lost!")
                if AI==1:
                    self.score2+=1
                else:
                    self.score1 += 1
                break

    def hostGameAIvsAI(self):
        """This method hosts the game with AI vs AI, first to 3 wins win!"""
        AI2Score = self.score2
        AI1Score = self.score1

        while True:
            print("AI1 score: " + str(self.score1))
            print("AI2 score: " + str(self.score2))
            self.AIvsAI(1)
            if self.score2 >= 3:
                self.p2Wins == True
                print("AI1 score: " + str(self.score1))
                print("AI2 score: " + str(self.score2))
                return
            if self.score1 >= 3:
                self.p1Wins == True
                print("AI1 score: " + str(self.score1))
                print("AI2 score: " + str(self.score2))
                return
            self.reset()
            self.AIvsAI(2)
            if self.score2 >= 3:
                self.p2Wins == True
                print("AI1 score: " + str(self.score1))
                print("AI2 score: " + str(self.score2))
                return
            if self.score1 >= 3:
                self.p1Wins == True
                print("AI1 score: " + str(self.score1))
                print("AI2 score: " + str(self.score2))
                return
            self.reset()
            

#Helper Functions
def replace(og, index, c):
    """Replaces character in string based on index."""
    new = og
    if index < len(og):
        new = og[0:index] + c + og[index + 1:]
    return new

def sortByLength(length, list):
    """This function sorts through the list and only keeps the words in the dictionary that is the same length as the given word."""
    for x in list:
        if len(x) == length:
            pass
        else:
            list.remove(x)
    return list


def sortList(indexGuess, letter, list):
    """This function sorts through every word in a list and removes the words without the same letters in the respective index."""
    for x in list: #for every word in list
        if letter in x: # if letter is in word
            indexNumber = x.index(letter) # indexNumber == to the index of x
            if indexNumber == indexGuess:
                pass
            else:
                list.remove(x)
        else:
            list.remove(x)
    return list

gameOn = True
def menu():
    """This function prints the menu"""
    print("Welcome to Hangman:")
    print()
    print("(0) Play human vs human")
    print("(1) Play human vs AI")
    print("(2) Play AI vs AI")
    print("(3) Quit")
    choice = int(input("Choose a gamemode: "))

    if choice == 0:
        p = HBoard()
        p.hostGameHuman()
    if choice == 1:
        p = HBoard()
        p.hostgameAIHuman()
    if choice == 2:
        p = HBoard()
        p.hostGameAIvsAI()
    if choice == 3:
        gameOn = False
        return


while gameOn == True:
    menu()
