#Day009
#Dic and nesting 

family = {
    "Mom" :  "is the mom", 
    "dad" : "is the dad",
    "Linwood Jr" : "is the son and is me",
    "oldest sister" : "is the oldest sister",
    "middle sister" : "is the middle sister",
    "twin sister" : "is my twin is sister"
    }
    
print("I am "+ family["Linwood Jr"])
print(family["twin sister"])
family["grandma"] = "The oldest in the family"
print(str(family))

for memember in family:
    print(memember + ':\t ' +family[memember])

student_scores = {
    "Harry" :81,
    "Ron" : 78,
    "Herminoe" : 99,
    "Draco" : 65,
    "Neville": 62, 
    "Jeff" : 85,
    "Matt": 89
}

student_grades = {}

for people in student_scores:
    if student_scores[people] > 91 and student_scores[people] < 100:
        student_grades[people] = "Outstanding"
    elif student_scores[people] > 81 and student_scores[people] < 90:
        student_grades[people] = "Exceeds Expections"
    elif student_scores[people] > 71 and student_scores[people] < 80:
        student_grades[people] = "Acceptable"
    elif student_scores[people] < 70:
        student_grades[people] = "Fail"
    else:
        print("Error")

print("This is the student scores\n\t" + str(student_scores))
print("This is the student grades\n\t" + str(student_grades))

travel_log={
    "USA" : {"cities_visited": ["Fayetteville","Indianapolis" "Nashville", "Detroit","Cincinnati","Myrtle Beach", "Austin", "Atlanta", "Phoniex", "Chicago", "San Fran", "Seattle", "Denver", "Las Vegas", "Kansas City", "Des Monies"],"total_visits": 20},
    "Mexico" : {"cities_visited": ["Mexico City","Iztapalapa de Cuitláhuac"], "total_visits": 2}
}


#Slient auction 
from os import system, name
bids = []
highestBid = 0
highestBidder = ""
def add_new_bid(name, bid):
    new_bids = {}
    new_bids["Name"] = name
    new_bids["Price/Bid"] = bid
    bids.append(new_bids)

print("Welcome to the slient auction\n")
name = str(input("Please enter your name\n"))
bid = int(input("Please enter your bid \n"))
add_new_bid(name,bid)

if bid > highestBid:
    highestBid = bid
    highestBidder = name
choice = str(input("Is there any other bidders \nY or N \n"))
while choice == "Y":
    system('clear')
    print("Welcome to the slient auction\n")
    name = str(input("Please enter your name\n"))
    bid = int(input("Please enter your bid \n"))
    if bid > highestBid:
        highestBid = bid
        highestBidder = name
    add_new_bid(name,bid)
    choice = str(input("Is there any other bidders \nY or N \n"))

else:
   print(f"Highest bidder is {highestBidder} at the price ${highestBid}")