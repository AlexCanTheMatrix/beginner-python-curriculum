import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
# Create a list of 4 car brands
car_brands = ["Toyota", "Ford", "BMW", "Tesla"]

# Print the first and last elements using indexing
print("First car brand:", car_brands[0])
print("Last car brand:", car_brands[-1])

# Add another brand using append()
car_brands.append("Honda")

# Print the updated list
print("Updated list:", car_brands)



# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
# Create a list of 5 numbers
numbers = [10, 20, 30, 40, 50]

# Print the number at index 2 (the 3rd item)
print("Number at index 2:", numbers[2])

# Insert a new number (e.g., 99) at index 2
numbers.insert(2, 99)

# Print the updated list
print("Updated list:", numbers)



# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then use a for loop to print each city.
# Create a list of 3 cities
cities = ["Tokyo", "Paris", "New York"]

# Print the length of the list using len()
print("Length of the list:", len(cities))

# Use a for loop to print each city
for city in cities:
    print(city)



# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
import random

# Create a list of 6 file extensions
extensions = ["txt", "pdf", "jpg", "png", "py", "csv"]

# Print a random one using random.choice()
random_extension = random.choice(extensions)
print("Random extension:", random_extension)

# Pop the element at index 3 (the 4th item, which is "png")
popped_item = extensions.pop(3)
print(f"Popped item at index 3: {popped_item}")

# Print the updated list
print("Updated list:", extensions)



# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then use a for loop to print all the names.
# Create a list of 8 names
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"]

# Find and print the name at the middle index using len()
# For 8 items, len(names) // 2 gives index 4 (the 5th name, "Emma")
middle_index = len(names) // 2
print("Name at the middle index:", names[middle_index])

# Use a for loop to print all the names
print("\nAll names in the list:")
for name in names:
    print(name)
