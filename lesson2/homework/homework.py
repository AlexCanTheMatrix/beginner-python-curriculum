# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
number1=input("Pick 1 random number")
number2=input("Pick another random number")
print("The qoutient is",int(int(number1)/int(number2)), "the remainder is", int(number1)% int(number2) )

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal=input("Pick your favorite animal")
color=input("Pick your favorite color")
print("A",color, animal ,"would be cool")
# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for n in range(0,11):
    print(n)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pp=input("How many push-ups can you do")
print("You cold do",int(pp)*7, "in a week" )

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for h in range(1,7):
    print(h*h