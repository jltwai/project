# Variables
    ## Making a contact management system. The given program declares two variables, name and age. Complete the code to output "name is age years old", where name and age are the declared variable values.
        ## name = "James"
        ## age = "42"
        ## print(name + " is " + age + " years old")
        # Improve the contact card program that we previously made using variables. Change the given code to take the name and age from user input and use them in the output.
name = input()
age = input()
print(name + " is " + age + " years old")


# if Statement & else Statement
    ## Making a program to take a year as input and output "Leap year" if it’s a leap year, and "Not a leap year", if it’s not.
        ## To check whether a year is a leap year or not, you need to check the following:
        ## 1) If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
        ## 2) If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
        ## 3) If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a leap year.
year = int(input())
if((year % 4 == 0) and (year % 100 != 0) or (year % 400 ==0)):
    print ("Leap year")
else:
    print("Not a leap year")

    ## caculate the gold's purity
        ## Purity chart we’ll be using:
            ## 24K – 99.9%
            ## 22K – 91.7%
            ## 20K – 83.3%
            ## 18K – 75.0%
        ## If the percentage is between 75 and 83.3, the gold is considered to be 18K.
        ## If it's between 83.3 and 91.7 - then it’s 20K, and so on.
        ## Given the percentage as input, output the corresponding Karat value, including the letter K.
purity = float(input())
if purity >= 75 and purity < 83.3:
    print("18K")
if 83.3 <= purity < 91.7:
    print("20K")
if 91.7 <= purity < 99.9:
    print("22K")
if purity >= 99.9:
    print("24K")


# while loop
    ## Making a game! The player tries to shoot an object and can hit or miss it.
        ## The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.
        ##This program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.
points = 100
n = 4

while n > 0:
    action = input()
    if action == "hit":
        points += 10
    elif action == "miss":
        points -= 20
    n -= 1

print(points)


# continue
    ## Making a ticketing system.
        ## The price of a single ticket is $100.
        ## For children under 3 years old, the ticket is free.
        ## This program needs to take the ages of 5 passengers as input and output the total price for their tickets.
total = 0
price = 100
num_ppl = 5

while num_ppl > 0:
    age = int(input())
    num_ppl -= 1
    if age < 3:
        continue
    total += 100

print(total)


# Control Flow -- BMI Calculator
    ## Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²
    ##The resulting number indicates one of the following categories:
        ## Underweight = less than 18.5
        ## Normal = more or equal to 18.5 and less than 25
        ## Overweight = more or equal to 25 and less than 30
        ## Obesity = 30 or more
    ## Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI categor
weight = int(input())
height = float(input())
BMI = weight / (height ** 2)

if BMI < 18.5:
    print("Underweight")
if 18.5 <= BMI < 25:
    print("Normal")
if 25 <= BMI < 30:
    print("Overweight")
if BMI >= 30:
    print("Obesity")


# Lists
    ## The seats in your ticketing program are stored in a 2D list. Each seat is assigned a letter code.
    ## Complete the program to take the seat row and column as input and output the corresponding code from the list (row and column indices start from 0).
seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]

row = int(input())
column = int(input())
print(seats[row][column])


# for loop
    ## Making a shopping cart program.
        ## The shopping cart is declared as a list of prices, and you need to add functionality to apply a discount and output the total price.
        ## Take the discount percentage as input, calculate and output the total price for the shopping cart.
        ## Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)
cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0
x = discount

for y in cart:
    total += y - (y * x / 100)
print(total)


# Ranges
    ## A group of buildings have restrooms on every 5th floor.
    ## For example, a building with 12 floors has restrooms on the 5th and 10th floors.
    ## Create a program that takes the total number of floors as input and outputs the floors that have restrooms.
n = int(input())

for i in range(1, n):
    if i % 5 == 0:
        print(i)


# Loop
## Sum of Consecutive Numbers
    ## Caculate the sum of the first N numbers
    ## Take a number N as input and output the sum of all numbers from 1 to N (including N).
N = int(input())
x = (range(1, N + 1))
print(sum(x))


# def function
    ## Feet to Inches Converter
        ## Making a function that converts a foot value to inches.
        ## 1 foot has 12 inches.
        ## Define a convert() function, that takes the foot value as argument and outputs the inches value.
feet = int(input())

def convert(feet):
    print(feet * 12)

convert(feet)


# def&return
    ## Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string.
def letter_count(text, letter): 
    x = (text.count(letter)) 
    return (x)

text = input()
letter = input()

print(letter_count(text, letter))


# function
    ## Search Engine
        ### working on a search engine. Watch your back Google!
        ### The given code takes a text and a word as input and passes them to a function called search().
        ### The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
text = input()
word = input()

def search(text, word):
    if word in text:
        return("Word found")
    else:
        return("Word not found")

print(search(text, word))
