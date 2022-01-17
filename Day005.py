#Day 005
#Loops
import random

fruits = ["Apple", "Peach", "Pear", "Grapes", "Lime"]

for fruit in fruits:
    print(f" The fruit of the day {fruit}")
###############################################################################
#student heights and could not use sum() function 

student_heights = input("Input a list of student heights \n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#print(student_heights)
total = 0
for students in student_heights:
    total += int(students)

print("The avgerage height for students:" + str(round(total/len(student_heights))))

#highest score in class 

student_scores = input("Input a list of students grade \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
#print(student_scores)

hightest_score =0 
for score in student_scores:
    if score > hightest_score:
        hightest_score = score
print(f"The hightest score in the class is {hightest_score}")

#For loop 

for number in range(1,30):
    print(str(number))
total =0 
for number in range(1,101):
    total += number
print(str(total))


#Adding all the even number from 1 to 100 
evenTotal= 0
for number in range(1,101):
    if number % 2 ==0:
        evenTotal += number
print(f"The total of all the even number from 1 to 100 is {evenTotal}")

evenTotal= 0
for number in range(1,101,2):
    evenTotal += number
print(f"The total of all the even number from 1 to 100 is {evenTotal}")



#FizzBuzz Again 
fizzCount = 0
buzzCount = 0
fizzBuzzCount = 0
sentence = ' '
for i in range(1,101):
    foo = i%3
    bar = i%5
    #print foo
    #print bar
    if (foo == 0 and bar == 0):
        sentence = sentence + "FizzBuzz" + "\n"
        fizzBuzzCount += 1
    elif (bar == 0):
        sentence = sentence + "Buzz" + "\n"
        buzzCount += 1
    elif (foo == 0):
        sentence = sentence + "Fizz" + "\n"
        fizzCount += 1
    else:
        sentence = sentence + str(i) + "\n"
    print(sentence)
    print(f"Fizz Count is: {fizzCount}")
    print(f"Buzz Count is: {buzzCount}")
    print(f"FizzBuzz Count is: {fizzBuzzCount}")

#Password Generator i cheated a little with the list to string conversation, used some of my old github code
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&']
print("Welcome to Jeff's password creator \n")
numberOfLetters = int(input("How many letters would you like \n"))
numberOfSymbols = int(input("How many symbols would you like \n"))
numberOfNumbers = int(input("How many numbers would you like \n"))

password = []

for value in range(numberOfLetters):
    randomNumber = random.randint(0,len(letters)-1)
    if randomNumber % 2 == 0 and value % 2 !=0:
        password.append(letters[randomNumber].upper())
    else:
        password.append(letters[randomNumber])
for value in range(numberOfNumbers):
        randomNumber = random.randint(0,len(numbers)-1)
        password.append(str(numbers[randomNumber]))

for value in range(numberOfSymbols):
        randomNumber = random.randint(0,len(symbols)-1)
        password.append(str(symbols[randomNumber]))

randomNumber = random.randint(1,9)
for x in range(0,randomNumber):
    random.shuffle(password)

passwordStr = ''.join([str(x) for x in password])
print(f"Here is your password: {passwordStr}")

