#Day012
#local scope and global scope 
#Namespaces

"""
number = 22 
def increase_numbers():
    number = 420
    number += 69
    print(f"The number in the function : {number}")
    
increase_numbers()
print(f"The number outside of the function: {number}")
"""
print("""   _____                       _   _            _   _                 _                
  / ____|                     | | | |          | \ | |               | |               
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|""")
print("Welcome to the Number Guessing Game!")
import random
theRandomNumber = random.randint(1, 100)
print(f"For testing the number is {theRandomNumber}")
print("Im thinking of a number between 1 and 100")
gameLevel = input("Choose a difficulty, type easy or hard:\n")
if gameLevel.lower() == 'easy':
    numberOfGuess = 10 
elif gameLevel.lower() == 'hard':
    numberOfGuess = 5
else:
    print("Stop Cheating")
def decreaseGuess():
    global numberOfGuess
    numberOfGuess = numberOfGuess -1 
    return numberOfGuess
while numberOfGuess > 0: 
    print(f" You have {numberOfGuess} attemps left to guess")
    guess = int(input("Please enter your guess:\t"))
    if guess > theRandomNumber:
        print("Too High")
        decreaseGuess()
    elif guess < theRandomNumber:
        print("Too low")
        decreaseGuess()
    elif guess == theRandomNumber:
        print(f"Some how you cheated you guessed correct, the random number is {theRandomNumber}")
        print(f"You had {numberOfGuess} attemps left")
        break
    else:
        print("ERROR ERROR ERROR ")
print(f"You ran out of guesses, the actually number is {theRandomNumber}")
