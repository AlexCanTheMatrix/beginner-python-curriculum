import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
# Create a list of 3 operating systems
# Create a list of 3 operating systems
os_list = ["Windows", "macOS", "Linux"]

# Print the last one using len()
# len(os_list) is 3, minus 1 gives index 2 (the last item)
print(os_list[len(os_list) - 1])

# Reverse the list and print it
os_list.reverse()
print(os_list)




# Problem 2
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
# Create a list of 5 error codes
error_codes = [400, 401, 403, 404, 500]

# Print how many there are
print(len(error_codes))

# Use a for loop to print each error code
for code in error_codes:
    print(code)



# Problem 3
# # Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random

# Create a list of 2 programming languages
languages = ["Python", "JavaScript"]

# Print a random one
print(random.choice(languages))

# Append another language and print the list
languages.append("Go")
print(languages)



# Problem 4
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
# Create a list of 6 passwords
passwords = ["pass123", "secret!", "admin2026", "qwerty", "letmein1", "securePass"]

# Print the one in the middle using len()
# For 6 items, len() // 2 gives index 3 (the 4th item)
middle_index = len(passwords) // 2
print(passwords[middle_index])

# Remove the first password in the list and print it
# pop(0) removes the item at index 0 and returns it
removed_password = passwords.pop(0)
print(removed_password)
