# Day003
#conditional statement 

#Theme park prices and enterance
bill = 0
print("Welcome to 6 Flags over GA \n")
#Ask user for height
height = int(input("What is your height in inches: \n"))
if height >= 40:
    print("You can ride rollercoasters !!!")
    #Ask user for age 
    age = int(input("How old are you \n"))
    if age > 18:
        print("Adults are $12.99 per ticket please\n")
        bill = bill + 12.99
    elif age < 18 and age > 12:
        print("Youths $7.99 per ticket please\n")
        bill = bill + 7.99
    else:
        print("Child are $5.99 per ticket please \n")
        bill = bill + 5.99
    #Ask user for a photo    
    userWantsPhoto = input("Would you like a photo: \nPlease Enter Y or N \t")
    if userWantsPhoto == 'Y':
        bill = bill + 3.99
        print(f"Your final bill is ${bill} will that be cash or card")
    else:
        print(f"Your final bill is ${bill} will that be cash or card")

else:
    print("Sorry you are too short for 6 Flags over GA \n")


#Odd or even 

number = int(input("Please enter a number \n # "))

if number %2 == 0:
    print(f"The number {number} is even ")
else:
    print(f"The number {number} is odd ")

#BMI calc with status 

print("Welcome to the BMI Calualtor")
height = float (int(input("Please enter your height in centimeters: \n") )/100 )
weight = int(input("Please enter your weight in kilograms: \n") )
bminumber = round(float( weight /(height * height)),2)

if bminumber <= 18.5:
    print(f" Your BMI is: {bminumber} and you are underweight")
elif bminumber < 25 :
    print(f" Your BMI is: {bminumber} and you are normal weight")
elif bminumber < 30 :
    print(f" Your BMI is: {bminumber} and you are overweight")
elif bminumber < 35 :
    print(f" Your BMI is: {bminumber} and you are obese")
else:
    print(f" Your BMI is: {bminumber} and you are clinically obese")


# leap year tester 

year = int(input("Please enter a year: \n"))



if year % 4 == 0:
  if year % 100 == 0 and year % 400 == 0: 
    print(f"Year {year} is a leap year")
  elif year % 100 == 0 and year % 400 != 0:
    print(f"Year {year} is NOT leap year")
  else:
      print(f"Year {year} is a leap year")
else: 
    print(f"Year {year} is a NOT leap year")


#Pizz calc
pizzaBill = 0
print("Welcome to CiCi's")
size = input("What size pizza do you want S ,M, or L \n")
moreP = input("Would like to add pepperoni on that pie: \nY or N \t")
extraCheese = input("Would like extra cheese on that pie: \nY or N \t")
if size == 'S':
    pizzaBill += 15
    if moreP == "Y":
        pizzaBill += 2
        if extraCheese == 'Y': 
            pizzaBill += 1
            print(f"Your total is {pizzaBill}")
    if extraCheese == 'Y': 
            pizzaBill += 1
            print(f"Your total is {pizzaBill}")
    print(f"Your total is {pizzaBill}")
if size == 'M':
    pizzaBill += 20
    if moreP == "Y":
        pizzaBill += 3
        if extraCheese == 'Y': 
            pizzaBill += 1
            print(f"Your total is {pizzaBill}")
    if extraCheese == 'Y': 
            pizzaBill += 1
            print(f"Your total is {pizzaBill}")
    print(f"Your total is {pizzaBill}")
if size == 'L':
    pizzaBill += 25
    if moreP == "Y":
        pizzaBill += 3
        if extraCheese == 'Y': 
            pizzaBill += 1
            print(f"Your total is {pizzaBill}")
    if extraCheese == 'Y': 
            pizzaBill += 1
            print(f"Your total is {pizzaBill}")
    print(f"Your total is {pizzaBill}")

#love calc 

print("Welcome to Love Calculator")
name1 = (input("Enter the lover 1 name:\n")).lower()
name2 = (input("Enter the lover 2 name:\n")).lower()
firstDigit = 0
secondDigit = 0 
firstDigit += name1.count('t') + name2.count('t')
firstDigit += name1.count('r') + name2.count('r')
firstDigit += name1.count('u') + name2.count('u')
firstDigit += name1.count('e') + name2.count('e')
secondDigit += name1.count('l') + name2.count('l')
secondDigit += name1.count('o') + name2.count('o')
secondDigit += name1.count('v') + name2.count('v')
secondDigit += name1.count('e') + name2.count('e')
print(f"Your True Love score is {firstDigit}{secondDigit}%")