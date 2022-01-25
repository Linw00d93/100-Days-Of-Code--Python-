#Day015
#Local Dev env Coffe Projacts


print("""   _____       __  __            __  __       _             
  / ____|     / _|/ _|          |  \/  |     | |            
 | |     ___ | |_| |_ ___  ___  | \  / | __ _| | _____ _ __ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` | |/ / _ \ '__|
 | |___| (_) | | | ||  __/  __/ | |  | | (_| |   <  __/ |   
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|_|\_\___|_|   """)


water = 300
milk = 200 
coffee = 44 
bank = 0
money = 0
makingCoffee = True
ePrice = 1.50
lPrice = 2.50
cPrice = 3.00

def askForMoney():
    global money
    print("Please insert coins")
    quarters = int(input("How many quarters:\t"))
    dimes = int(input("How many dimes:\t"))
    nickles = int(input("How many nickles:\t"))
    pennies = int(input("How many pennies:\t"))
    money = round(quarters * .25 + dimes * .10 + nickles * 0.05 + pennies * 0.01,2)



while makingCoffee == True:
    choice = input("What would you like\n")


    if choice.lower() == "espresso":
        if water >= 50 and coffee >= 18: 
            askForMoney()
            if money > lPrice:
                change = round(money - ePrice,2)
                bank = bank + ePrice
                print(f"Here is your change ${change}")
                water = water - 50
                coffee = coffee - 18
            if money < ePrice:
                print("Not Enough money")
                break
        else: 
            print("Out of Resources")


    if choice.lower() == "latte":
        if water >= 200 and coffee >= 24 and milk >= 150: 
            askForMoney()
            if money > lPrice:
                change = round(money - lPrice,2)
                bank = bank + lPrice
                print(f"Here is your change ${change}")
                water = water - 200 
                coffee = coffee - 24
                milk = milk - 150
            if money < lPrice:
                print("Not Enough money")
                break
        else:
            print("Out of Resources")

    if choice.lower() == "cappuccino":
        if water >= 250 and coffee >= 24 and milk >= 100 : 
            askForMoney()
            if money > cPrice:
                change = round(money - cPrice,2)
                bank = bank + cPrice
                print(f"Here is your change ${change}")
                water = water - 250 
                coffee = coffee - 24 
                milk = milk - 100 
            if money < cPrice:
                print("Not Enough money")
                break
        else:
            print("Out of Resources")
    if choice.lower() == "report":
        print(f"Water: \t{water}\nCoffee:\t{coffee}\nMilk: \t{milk}\nBank:\t${bank}\n")
    if choice.lower() == "quit":
        makingCoffee == False
        break
