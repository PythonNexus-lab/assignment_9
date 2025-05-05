# a. Create a list of 10 numbers
numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5, 10]

# b. Sum all elements
total = sum(numbers)

# c. Display the list and total
print("List:", numbers)
print("Total Sum:", total)


# a. Create a list of 5 fruit names
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# b. Display all contents
print("Fruits:", fruits)

# c. Display fruit at index 2
print("Fruit at index 2:", fruits[2])

# d. Add a new fruit
fruits.append("grape")

# e. Display updated list
print("Updated Fruits:", fruits)


# a. Accept space-separated numbers from user
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# b. Total sum
total = sum(numbers)

# c. Average value
average = total / len(numbers)

# d. Max and Min
maximum = max(numbers)
minimum = min(numbers)

# Display results
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Max:", maximum)
print("Min:", minimum)


import statistics

# a. Ask user for numbers
data = input("Enter at least 5 numbers separated by space: ")
numbers = list(map(int, data.split()))

# b. Calculate stats
minimum = min(numbers)
maximum = max(numbers)
average = sum(numbers) / len(numbers)
median = statistics.median(numbers)

# c. Sorted list
sorted_list = sorted(numbers)

# Display
print("Numbers:", numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Median:", median)
print("Sorted List:", sorted_list)


# a. Empty shopping list
shopping_list = []

# b. Input 5 items
for i in range(5):
    item = input(f"Enter item {i+1}: ")
    shopping_list.append(item)

# c. Display full list
print("Your Shopping List:", shopping_list)

# d. Remove one item
to_remove = input("Enter item you purchased to remove it: ")
if to_remove in shopping_list:
    shopping_list.remove(to_remove)
    print(f"{to_remove} removed.")
else:
    print(f"{to_remove} not found in the list.")

# e. Display updated list
print("Updated Shopping List:", shopping_list)

