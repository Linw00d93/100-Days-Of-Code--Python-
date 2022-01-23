#Day011
#Blackjack
import random 
import time
playerHand = []
dealerHand =[]

print("""  ____  _            _        _            _    
 |  _ \| |          | |      | |          | |   
 | |_) | | __ _  ___| | __   | | __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   < |__| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\\n""")

print("Welcome to simple blackjack, there are no face cards and no betting")

print(f"Players hand: \t {playerHand}")
print(f"Dealers hand: \t {dealerHand}")
print("Drawing first cards")
theRandomCard = random.randint(1, 10)
playerHand.append(theRandomCard)
theRandomCard = random.randint(1, 10)
dealerHand.append(theRandomCard)
time.sleep(3)
gamePlaying = True
print(f"Players hand: \t {playerHand}")
print(f"Dealers hand: \t {dealerHand}")
while gamePlaying == True:
    playerChoice = input("What would you like to do next?\n Hit or Stay\t")
    
    if playerChoice.lower() == "hit":
        theRandomCard = random.randint(1, 10)
        playerHand.append(theRandomCard)
        print(f"Players hand: \t {playerHand}")
        print(f"Dealers hand: \t {dealerHand}")
        if sum(playerHand) > 21:
            print(f"Player Bust with {playerHand}")
            break
    elif playerChoice.lower() == "stay":
        print(f"Players hand: \t {playerHand}")
        print(f"Dealers hand: \t {dealerHand}")
        
        while sum(dealerHand) < 22:
            theRandomCard = random.randint(1, 10)
            dealerHand.append(theRandomCard)
            print("Dealer will now draw")
            time.sleep(3)
            print(f"Players hand: \t {playerHand}")
            print(f"Dealers hand: \t {dealerHand}")
            if sum(dealerHand) == 21:
                print(f"Deal WON with 21\t {dealerHand}")
                gamePlaying == False
                break
            if sum(dealerHand) > sum(playerHand) and sum(dealerHand) <= 21:
                print(f"Dealer WON with higher score\t {dealerHand} \t {sum(dealerHand)}")
                print(f"Players Hand {playerHand} \t {sum(playerHand)}")
                gamePlaying == False
                break
            if sum(dealerHand) > 21:
                print(f"Dealer bust \t {dealerHand}")
                print(f"Player won with\t {playerHand}")
                gamePlaying == False
                break