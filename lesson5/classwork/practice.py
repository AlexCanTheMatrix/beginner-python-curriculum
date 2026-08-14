# Problem 1
# Search the list and print whether "banana" is found.
fruits = ["apple", "orange", "banana", "grape"]

if "banana" in fruits:
    print("banana is found")
else:
    print("banana is not found")



# Problem 2
# Count how many numbers are greater than 10 in the list.
numbers = [4, 18, 2, 30, 7, 12]
numbers = [4, 18, 2, 30, 7, 12]
count = 0

for num in numbers:
    if num > 10:
        count = count + 1

print(count)



# Problem 3
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
numbers = [4, 11, 22, -6, 3]
total = 0

for num in numbers:
    total = total + num

print(total)



# Problem 4
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
numbers = [-9, 17, 5, -3, 0]
biggest = numbers[0]

for num in numbers:
    if num > biggest:
        biggest = num

print(biggest)



# Problem 5
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
numbers = [8, 3, 15, 22, 11, 6]
total = 0

for num in numbers:
    if num % 2 == 0:
        total = total + num

print(total)
