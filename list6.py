# Create a list
numbers = [10, 20, 30, 40, 50]

# Display the original list
print("Original list:", numbers)

# Search for a number
x = int(input("Enter a number to search: "))

if x in numbers:
    print("Number found")
else:
    print("Number not found")

# Update an element
numbers[0] = 100
print("After update:", numbers)

# Add an element using append()
numbers.append(60)
print("After append:", numbers)

# Remove an element using remove()
numbers.remove(30)
print("After remove:", numbers)

# Filter even numbers using list comprehension
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)

# Reverse the list
numbers.reverse()
print("After reversing:", numbers)
