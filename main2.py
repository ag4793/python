# what are variables?

# there are differnt types of variables
# strings are text
name = "John" # quotation marks
name2 = "Lucy"
# integers are whole numbers
num1 = "10" # no quotation marks
num2 = 20
print(int(num1) + num2)
# a plus sign between two variables its called 
#concatenation
# type casting when you convert a 
# variable from one type to another
# print(name +"and"+ name2 + "have"+ num1 + str(num2) + "apples")
# f strings allow us to insert variables into strings
# using f beofre the string
print(f"{name} and {name2} have {num1 + num2} apples")

# floats are decimal numbers
dollars = 10.99
# it can be postive or negative
print(f"{name} has {dollars} dollars")
# booleans are true or false
is_student = True
# it can be true or false
print(f"{name} is a student: {is_student}")
# lists are collections of values
# dictionaries are collections of key-value pairs
# problem set #1 
# 1. create 4 different types of variables

# 2. print them out

# 3. use f strings to format the strings














# if condionals
# if statements are used to check if a conditon is True or False
# if conditon is true, do something
# if conditon is false, do something else

# if condional statements always start with if
# and depend on a boolean value  (true or false)
# example
classStarted = True
if classStarted:
    print("class has started")
else:
    print("class has not started")

# logical and comparison operator 
# == equal to
# != not equal to 
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# and logical operators
# or logical operators
# not logical operators
# example
age = 18
if age >= 18:
    print("you are an adult")
elif age == 17:
    print("you are almost an adult")
else:
    print("you are a minor")

#problem set #2
# 1. create a program that checks if a number
# is even or odd
# 2. ask user for a number
number = int(input("what is your number"))
# 3. check if number us even or odd
if number % 2 == 0:
    print (f"{number} is even")
else:
    print(f"{number} is odd")
