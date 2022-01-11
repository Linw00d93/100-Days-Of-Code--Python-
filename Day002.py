#Day 002 
#Data Types

#tip calculator

print("Welcome to the Tip Calculator!")
bill = float(input("What is the total amount of the bill: \n$"))
howManyPeople = int(input("How many people are in your party: \n"))
tip = float(input("What percentage would you like to tip: \n"))
howEachPersonPays = round((((bill * (tip/100)) + bill)/howManyPeople),2)
print("Each Person should pay: $" + str(howEachPersonPays))

#BMI 

print("Welcome to the BMI Calualtor")
height = float (int(input("Please enter your height in centimeters: \n") )/100 )
weight = int(input("Please enter your weight in kilograms: \n") )
print(" Your BMI is: " + str (int( weight /(height * height) ) ) )

#For USA lol 
print("Welcome to the BMI Calualtor")
height = int(input("Please enter your height in inches: \n") )
weight = int(input("Please enter your weight in pounds: \n") )
print("Your BMI is: " + str (int( (703 * weight )/(height * height) ) ) )

#Your life in weeks

print("Your life in weeks")
age = int(input("Please enter your age \n"))
years = 90 - age
months = (90 - age)* 12
days = (90 - age) * 365
weeks = (90 - age) * 52
hours = (90- age) * 8760
print(f"You have {years}-years or {months}-months or {weeks}-weeks or {days}-days or {hours}-hours till you are 90 years old")

"""
#Extra stuff 
randomNumber = 69 
print(f"My is Elon favorite number {randomNumber}")
number = int(input("Please enter a two digit number: \n"))
total = number[0] + number[1]
print("The total sum of the two digits in " + str(number) + "equals: " + str(total))
print(69 ** 420)
print("Linwood"[3])
print(type(bill))
print(type(howEachPersonPays))
print(type("Linwood Is The Best, Duh !!!"))
print(str(float(int(69))))



"""