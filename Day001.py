#Day 001 
#Band Generator
"""
 print("Hello World")
 number = 1 
 boolean = true
 string = "my name is"
 character = 'a'
 print(number)

"""
print("Welcome to the Band Generator!")
city = input("What is the name of the city you are from: \n")
petName = input("What is your pet's name or nickname: \n")
print("Your band name is " + city + " " + petName) 

#Letter counter 
#In real life i would use a function to count the number of letters in a string and also check to seee if the input has numbers,spaces, or special characters.
#it would take longer to excute but would have a correct answer 

lettersInName = len(input("What is your name: \n"))
print("Your name has " + str(lettersInName) + " letters in it.")