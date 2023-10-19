# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of a list
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modifying elements of a list
my_list[2] = 10
print("Updated list:", my_list)

# Adding elements to a list
my_list.append(6)
print("List after appending 6:", my_list)

# Removing elements from a list
removed_element = my_list.pop(1)
print("List after removing element at index 1:", my_list)
print("Removed element:", removed_element)

# Iterating through a list
print("Elements of the list:")
for element in my_list:
    print(element)

# List slicing
subset = my_list[1:3]
print("Subset of the list:", subset)

# Finding the length of a list
list_length = len(my_list)
print("Length of the list:", list_length)
