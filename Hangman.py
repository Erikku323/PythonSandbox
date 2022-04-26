#Hangman a simple game of hangman based on a small list of words more words can be added to the "word list"



HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random

wordList = ["monkey","cow","chicken","rooster","banana","turkey","vampire"]

word = wordList[random.randint(0,len(wordList) - 1 )].lower()

print(word)

endGame = False
guesses = []
numOFGuess = 0
HangmanLvl = 0
def MakeGuess():
    validInput = False
    while validInput == False:
        guess = input("Make a guess\n")
        if len(guess) > 1:
            print("Please use only 1 letter\n")
        elif guesses.__contains__(guess.lower()) == True:
            print("You have already made that guess\n")
        elif guess.isalpha() == False:
            print("Please type a letter!\n")
        else:
            validInput = True
    return guess


extendedWord = []

for letters in word:
    extendedWord.append("_")

print(extendedWord)
print("")

while endGame == False:


    guesses.append(MakeGuess())

    if word.__contains__(guesses[numOFGuess]) == False:
        HangmanLvl = HangmanLvl + 1
    else:
      #  print("Correct")
        i = 0
        for letters in word:
            if guesses.__contains__(letters):
                extendedWord[i] = letters
            else:
                extendedWord[i] = "_"
            i = i + 1

    if extendedWord.__contains__("_") == False:

        print("You Win!")
        endGame = True
    elif HangmanLvl > (len(HANGMANPICS) - 1) :
        print("You Lose!")
        print("The word was " +  word)
        endGame = True
    if HangmanLvl > len(HANGMANPICS) - 1:
        HangmanLvl = len(HANGMANPICS) - 1
        print(HangmanLvl)


    print(HangmanLvl)
    print("")
    print(HANGMANPICS[HangmanLvl])
    print("")
    print(extendedWord)
    print("")

    if endGame == False:
        print("you have already picked")
        print(guesses)

print("\nGame complete")

