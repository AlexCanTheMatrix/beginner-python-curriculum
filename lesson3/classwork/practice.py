# Problem 1
# Ask the user to enter their height in centimeters.
# Print "Tall" if the height is greater than 170, otherwise print "Short".
height = int(input("How tall are you in cm"))
if height>= 170:
    print("you are tall")
else:
    print("you are short")
# Problem 2
# Ask the user for their age.
# If they are 18 or older, print "Adult", else print "Minor".
age = int(input("How old are you"))
if age>= 18:
    print("Adult")
else:
    print("Minor")
# Problem 3
# Ask the user to enter a number.
# Print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5,
# print "FizzBuzz" if divisible by both 3 and 5,
# otherwise print the number itself.
num = int(input("Pick a random number"))
if num%3 == 0:
    print("Fizz")
if num%5 ==0:
    print("Buzz")
if num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
# Problem 4
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."
age = int(input("How old are you"))
height = int(input("How tall are you"))
if age>= 10 and height>= 120:
    print("You can ride")
else:
    print("Sorry you can't ride")
# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."
# Ask the user for a number
user_input = input("Enter a number: ")
number = int(user_input)

# Check the conditions
if number % 3 == 0 and (number < 0 or number > 100):
    print("Weird number!")
else:
    print("Normal number.")
