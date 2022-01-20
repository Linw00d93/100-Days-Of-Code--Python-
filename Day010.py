#Day010
#Calc
#Functions with outputs
def addition(num1,num2):
    total = num1+num2
    return total
def subtration(num1,num2):
    total = num1-num2
    return total
def division(num1,num2):
    total = num1/num2 
    return total
def multiplication(num1,num2):
    total = num1 * num2 
    return total 
history =[]
keepDoingMath = True
print("Hello welcome to my simple calc")
while keepDoingMath == True:
    
    choice = input(" Which math function would you like to complete \n options are: + - / and * \n")

    if choice == '*':
        num1 = float(input("Please enter first number \n"))
        num2 = float(input("Please enter second number \n"))
        multiplication(num1,num2)
        print(f"The total of {num1} * {num2} equals {multiplication(num1,num2)}")
        history.append(f"The total of {num1} * {num2} equals {multiplication(num1,num2)}")
    elif choice == '+':
        num1 = float(input("Please enter first number \n"))
        num2 = float(input("Please enter second number \n"))
        addition(num1,num2)
        print(f"The total of {num1} + {num2} equals {addition(num1,num2)}")
        history.append(f"The total of {num1} + {num2} equals {addition(num1,num2)}")
    elif choice == '-':
        num1 = float(input("Please enter first number \n"))
        num2 = float(input("Please enter second number \n"))
        subtration(num1,num2)
        print(f"The different between {num1} and {num2} equals {subtration(num1,num2)}")
        history.append(f"The different between {num1} and {num2} equals {subtration(num1,num2)}")
    elif choice == '/':
        num1 = float(input("Please enter first number \n"))
        num2 = float(input("Please enter second number \n"))
        division(num1,num2)
        print(f"The {num2} goes into {num1} , {division(num1,num2)} times")
        history.append(f"The {num2} goes into {num1} , {division(num1,num2)} times")
    else:
        print("ERROR ERROR ERROR Please Try Again ")
    
    mathChoice = input("Would you like to continue to do math Y or N \n")
    mathChoice = mathChoice.upper()
    if mathChoice == "N":
        print("Goodbye")
        break; 
    elif mathChoice == "HISTORY":
        print(str(history))
