#Day006
#Functions and While Loops
import time



print("Linwood")
num_char = len("Linwood")
print(num_char)

def linwood():
    print("where is the food")
    print("when do we nap")

linwood()


def fizzBuzz(number):
    #FizzBuzz Again 
    fizzCount = 0
    buzzCount = 0
    fizzBuzzCount = 0
    sentence = ' '
    for i in range(1,number + 1):
        foo = i%3
        bar = i%5
        #print foo
        #print bar
        if (foo == 0 and bar == 0):
            print("FizzBuzz")
            fizzBuzzCount += 1
        elif (bar == 0):
            print("Buzz")
            buzzCount += 1
        elif (foo == 0):
            print("Fizz")
            fizzCount += 1
        else:
            print(str(i))
    print(f"Fizz Count is: {fizzCount}")
    print(f"Buzz Count is: {buzzCount}")
    print(f"FizzBuzz Count is: {fizzBuzzCount}")

fizzBuzzNumber = int(input("To what number would you like to see Fizz Buzz be executed to \n"))


fizzBuzz(fizzBuzzNumber)


def countdown(stopNumber):
    print("Are you ready? \n")
    while stopNumber > 0:
        print(stopNumber)
        stopNumber = stopNumber - 1 
        time.sleep(1)

    print("BING BONG DONE !!!!!!")

stopNumber = int(input("What number would you like to count down from\t"))

countdown(stopNumber)
