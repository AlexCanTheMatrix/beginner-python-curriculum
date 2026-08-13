# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
Score1 = int(input("What did you get on the first test"))
Score2 = int(input("What did you get on the second test"))
if Score1>=50 and Score2>=50:
    print("You passed both tests")
elif Score1>= 50 or Score2>= 50
print("You passed one and failed one")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
# Ask user if they brought lunch and water (yes/no)
lunch = input("Did you bring lunch? (yes/no): ").strip().lower()
water = input("Did you bring water? (yes/no): ").strip().lower()

# Check the conditions
if lunch == "yes" and water == "yes":
  print("You're fully ready!")
elif lunch == "yes" or water == "yes":
  print("You're somewhat ready.")
else:
  print("You're not ready.")



# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
# Ask user if they brought lunch and water (yes/no)
lunch = input("Did you bring lunch? (yes/no): ").strip().lower()
water = input("Did you bring water? (yes/no): ").strip().lower()

# Check the conditions
if lunch == "yes" and water == "yes":
    print("You're fully ready!")
elif lunch == "yes" or water == "yes":
    print("You're somewhat ready.")
else:
    print("You're not ready.")



# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
# Ask the user for a test score (0-100) and convert it to an integer
score_input = input("Enter your test score (0-100): ").strip()
score = int(score_input)

# Print the grade based on score
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
# Ask the user for two numbers and convert them to integers
num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())

# Check the conditions:
# "Divisible by 5" means the remainder after dividing by 5 is 0 (% 5 == 0)
# "Not divisible by 2" means the remainder after dividing by 2 is not 0 (% 2 != 0)

condition1 = (num1 % 5 == 0 and num2 % 2 != 0)
condition2 = (num2 % 5 == 0 and num1 % 2 != 0)

if condition1 or condition2:
    print("Interesting pair!")
else:
    print("Plain pair.")
