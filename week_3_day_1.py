# # Week3
# # This week we will work on :
# # Working With Strings


# # 1.   Working With Numbers
# # 2.   Getting Input From Users




# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game




































# # Review
# create variables for the following :
# 1. age
age = 16 #integer variable
# 2. name
name = "Maxwell" #string variable
# 3. song
song = "Blizzard" #string variable
# 4. food
food = "fries" #string variable
# 5. number
number = 1000 #integer variable

teammate = "Pancho" #string variable

# #now include the variables you just made print in the following...


# Once upon a time, there was a [age] old coder named [name].
#concantation --- + around your variables
#print("Once upon a time, there was a " + str(age) + " year old coder named " + name + ".")
#print("There was a number " + str(number) + " as well")
#put the age and number in a new sentence
#print("He was " + str(age) + " and his lucky number is " + str(number) + ".")
date_of_birth = 2021
number2 = 123
number3 = 123.456
number4 = 123.33
number5 = 4555
#create a sentence of all of the above :trollface:
#print("The year is " + str(date_of_birth) + " even though it's not. Anyways, here's some numbers. " + str(number2) + " and " + str(number3) + " and "+ str(number4) + " and "+ str(number5) + ".")
# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
#print(f"the date of birth is {date_of_birth} and the number is
      #{number2} and the number is {number3} and the number is
      #{number4}and the number is {number5}")

# Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
##########################################################################################

print(f"Once upon a time, there was a {age} old coder named {name}.")
print(f"{name} liked to hum the song {song} while coding. It was so annoying that their teammate {teammate} would throw {food} until {name} would stop singing.")
print(f"Still, {name} was the best coder on the team and could write about {number} lines of code every day, double the code {teammate} could do. Maybe {song} was {name}'s secret power?")
















##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"


# Here are some exercises to practice the rules:


# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# firstName
# lastName
# emailAddress
# percent
# variableName
# Zero
# list #this is a reserved word in python
#(you can't use it for yourself)

# Creating Valid Names: Create valid names for the following descriptions:


# The first name of a person = firstName
# The last name of a person lastName
# The email address of a person = emailAddress
# The percentage of marks obtained by a student = percent
# A variable to store the number of items in a shopping cart = store




# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# first_name = valid
# lastName = valid
# email_address = valid
# percentage = valid
# variable_name = valid
# 1_variable = invalid
# email@address = invalid
# percentage% = invalid
# i = invalid
















############################################################################################


# # **Working with** **numbers** **bold text**
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


##########################################################################################
# #addition
#print (2+1)
# #multiplication
#print(2*2)
# #division
#print(6/2)
# #modulo
#print(7%4) #remainder of 7/4
# #powers
#print(5**3) # 5 to the power of 3
# #get the max and min of a number
#print("The max of 2 and 3 is",max (2,3))
#Max means the highest number
#print("The min of 2 and 3 is",min (2,3))
# Min means the lowest number

# #round a number
#print("Round 3.9 is",round(3.9))
# # absolute value
#print("The absolute value of -3 is",abs(-3))
# absolute value is the distance from zero; thus, it will always be positive.
# # order of operations
#print("2 + 10 * 10 + 3 is",2 + 10 * 10 + 3)
# #to do more you need to import special math libraries from python
from math import *
# #this goes out and grabs some different math functions we can use
# #floor method
#print("The floor of 3.7 is",floor(3.7))
#Floor means round down
#print("The floor of 9.5 is",floor(9.5))
# #ceil method
#print("The ceil of 3.7 is",ceil(3.7))
#ceil means round up
#print("The ceil of 4.3 is",ceil(4.3))
# #sqrt method














##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
#name = input("what is your name?")
#print("Hello,", name)
# # basic math calculator
# #ask the user for 2 numbers
#num1 = int(input("Enter in a number:"))
#num2 = int(input("Enter in another number:"))
# # print out a statement where you:
# # add them together
#print(num1+num2)
# #multiply
#print(num1*num2)
# # find the max number
#print(max(num1,num2))
# # find the remainder of the numbers
#print(num1%num2)
# #round one number
#print(round(num1))



##########################################################################################
# CALCULATOR APP WOOHOO #

num1 = int(input("Enter in a number:"))
num2 = int(input("Enter in another number:"))
print(num1-num2)
print(num1/num2)
print(min(num1,num2))
print("The absolute value of your first number is",abs(num1))
print("The floor of your first number is",floor(num1))
print("The ceil of your second number is",ceil(num2))
print("The square root of your first number is",sqrt(num1))

##########################################################################################
# # mad libs game
color = input("Enter a color.")
plural_noun = input("Enter a plural noun:")
celebrity = input("Enter a celebrity:")
print("Roses are", color)
print(plural_noun, "aren't blue")
print("I love", celebrity)
# # On to codehs.com







