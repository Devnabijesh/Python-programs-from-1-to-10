# Create two dictionaries
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"d": 40, "e": 50, "f": 60}

# Sort the first dictionary
sorted_dict = dict(sorted(dict1.items()))
print("Sorted dictionary:", sorted_dict)

# Merge two dictionaries
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

# Create a list with repeated elements
items = ["a", "b", "a", "c", "b", "a"]

# Count the frequency of each element
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequency count:", frequency)

# Create two sets
set1 = {"a", "b", "c", "d"}
set2 = {"c", "d", "e", "f"}

# Find common elements
common = set1.intersection(set2)
print("Common elements:", common)

# Find unique elements in set1
unique_set1 = set1.difference(set2)
print("Unique elements in set1:", unique_set1)

# Find unique elements in set2
unique_set2 = set2.difference(set1)
print("Unique elements in set2:", unique_set2)

# Find elements unique to either set
unique_elements = set1.symmetric_difference(set2)
print("Unique elements:", unique_elements)