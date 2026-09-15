# Accept comma-separated numbers from the user
numbers = input("Enter comma-separated numbers: ")

# Generate a list
number_list = numbers.split(",")

# Generate a tuple
number_tuple = tuple(number_list)

# Display the list
print("List:", number_list)

# Display the tuple
print("Tuple:", number_tuple)

# Display the total number of elements
print("Total number of elements:", len(number_list))

# Display the first element
print("First element:", number_list[0])

# Display the last element
print("Last element:", number_list[-1])

# Display the list in reverse order
print("Reverse order:", number_list[::-1])