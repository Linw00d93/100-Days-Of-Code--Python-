#Day008 
#Function
import time

listOfLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encode(word,space):
    newLetter = 0
    space = int(space)
    word = str(word)
    newWord = word
    print("encode")
    time.sleep(3)
    for letter in range(0,len(word)):
        newLetter = 0
        ogLetter = word[letter]
        newLetter += int(listOfLetter.index(ogLetter))
        newLetter += space
        if newLetter > len(listOfLetter):
            newLetter = newLetter - len(listOfLetter)
            replace = word[letter]
            newLetterForWord = listOfLetter[newLetter]
            newWord = newWord.replace(newWord[letter],listOfLetter[newLetter])
        else:
            replace = word[letter]
            newLetterForWord = listOfLetter[newLetter]
            newWord = newWord.replace(newWord[letter],listOfLetter[newLetter])
    print(f"The old word is {word} and the encrypted word is {newWord}")

def decode(word,space):
    print("decode")
    time.sleep(3)
    newLetter = 0
    space = int(space)
    word = str(word)
    newWord = word
    for letter in range(0,len(word)):
        newLetter = 0
        ogLetter = word[letter]
        newLetter += int(listOfLetter.index(ogLetter))
        newLetter = newLetter - space
        if newLetter > len(listOfLetter):
            newLetter = newLetter + len(listOfLetter)
            replace = word[letter]
            newLetterForWord = listOfLetter[newLetter]
            newWord = newWord.replace(newWord[letter],listOfLetter[newLetter])
        else:
            replace = word[letter]
            newLetterForWord = listOfLetter[newLetter]
            newWord = newWord.replace(newWord[letter],listOfLetter[newLetter])
    print(f"The old word is {word} and the encrypted word is {newWord}")


userAnswer = str(input("Would you like to decode or encode: \n"))
if str(userAnswer) == "encode":
    word = input("What word would you like to encode: \n")
    space = input("How many space would you like to shift in encoding \n")
    encode(word,space)
elif str(userAnswer) == "decode":
    word = input("What word would you like to decode: \n")
    space = int(input("How many space would you like to shift in decoding \n"))
    decode(word,space)
else:
    print(f"Looks like you did not enter encode or decode you entered: {userAnswer}")
