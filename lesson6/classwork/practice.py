# Problem 1
# Write a function that returns your favorite fruit and print it.
def get_favorite_fruit():
    return "Mango"


print(get_favorite_fruit())



# Problem 2
# Write a function that takes one parameter num.
# The function should return the value of num multiplied by 2.
def multiply_by_two(num):
    return num * 2



# Problem 3
# Create a variable for a book, then print it.
# Modify it inside a function and print it again.
book_title = "The Hobbit"
print(book_title)


def modify_book():
    global book_title
    book_title = "The Lord of the Rings"


modify_book()
print(book_title)



# Problem 4
# Use a for loop to print the numbers from 1 to 7 (inclusive).
for n in range(1,8):
    print(n)


# Problem 5
# Use a for loop to print each element in the list.
items = ["chair", "table", "desk"]
for item in items:
    print(item)

