#HANGMAN 


print(""" _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """)

"""
numberOfTries = 10 
gameIsOn = True 
print("Welcome to hangman")
while gameIsOn == True: 
    guess = input("Please enter a letter for your guest")
    if guess in word  == True:
"""
import random
import time

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



randomNumber = random.randint(0,5)
List = ["export", "fabric", "junior", "letter", "matter", "narrow"]
guessLetter = ["_","_","_","_","_","_"]
playing = True
guessCount = 15
hangManWord = List[randomNumber]
hmwList = list(hangManWord)




print("Welcome to HangMan your word has six letters")
print("and you have 10 guesses to guess the word")
time.sleep(1)
while guessCount != 0:
    if guessCount >= 14:
        print(stages[6])
    elif guessCount <= 12:
        print(stages[5])
    elif guessCount <= 10:
        print(stages[4])
    elif guessCount <= 8:
        print(stages[3])
    elif guessCount <= 6:
        print(stages[2])
    elif guessCount <= 4:
        print(stages[1])
    elif guessCount < 2:
        print(stages[0])
        print("Game Over You Lost")
        break
    print("Would you like to guess the word or guess a letter")
    print("Type word for word guess or letter for letter guess")
    raw = input()
    userInput = raw.lower()
    print (userInput)
    
    if userInput == "word":
        print("Please enter your guess")
        userInputWord = input()
        if userInputWord == hangManWord:
            print("You guess the word correctly !!!")
            print("The word was:" )
            print(hangManWord)
            print("The number of guess left:")
            print(guessCount)
            print("Great Game !!")
            exit()
        else:
            print("Sorry that is not the word")
            guessCount= guessCount - 1
            print(guessCount)
            break
    elif userInput =="letter":
        print(guessLetter)
        print("Please enter your letter guess")
        userInputLetter= input()
        letterGuessed = hangManWord.find(userInputLetter)
        if letterGuessed > -1:
            print("Your letter was found in the word")
            if hmwList == 0:
                guessLetter[0] = userInputLetter
                del hmwList[0]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 1:
                guessLetter[1] = userInputLetter
                del hmwList[1]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 2:
                guessLetter[2] = userInputLetter
                del hmwList[2]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 3:
                guessLetter[3] = userInputLetter
                del hmwList[3]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 4:
                guessLetter[4] = userInputLetter
                del hmwList[4]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 5:
                guessLetter[5] = userInputLetter
                del hmwList[5]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 6:
                guessLetter[6] = userInputLetter
                del hmwList[6]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
        else:
            print("the letter is not found within the word")
            guessCount = guessCount - 1
            print(guessCount)
            
    else:
        print(" ERROR ERROR ERROR")