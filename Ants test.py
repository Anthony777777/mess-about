#this is my first test to see my undertsanding

name = input ("What is your Name? ")
#stops the user not entering anything
while name == "":
    name = input ("What is your Name? ")
else: print ("Hello " + name.capitalize())

book = input("What is your Favorite Book? ")
while book == "":
    book = input("What is your Favorite Book? ")
else: print ("Hello, i see your favorite book is: " + book.capitalize())


from datetime import date
birthdate = int(input("What year were you born? "))
def age(birthdate):
    today = date.today()
    return today.year - birthdate
print ("My records indicate you are? ", age(birthdate))
if age(birthdate) >= 30:
    print("You are very old")
if age(birthdate) < 30:
    print ("You are still young, Congrats!! ")

Dating_status = input ("Are you single? ")
if Dating_status == "yes":
    print("Congrats!! ")
elif Dating_status == "no":
    print ("That's ok as long as you are happy ")
else: print("Fantastic ")

print("Here is your random activity:")
from random import randint
date_night = ["netflix", "Cinema", "Go for a walk", "Board Games"]
computer = date_night[randint(0,3)]
print(computer)
