# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing elements of a dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Modifying elements of a dictionary
my_dict['age'] = 26
print("Updated dictionary:", my_dict)

# Adding new key-value pairs to a dictionary
my_dict['occupation'] = 'Engineer'
print("Dictionary after adding occupation:", my_dict)

# Removing key-value pairs from a dictionary
removed_value = my_dict.pop('city')
print("Dictionary after removing 'city':", my_dict)
print("Removed value:", removed_value)

# Iterating through a dictionary
print("Key-Value pairs in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key is in the dictionary
if 'name' in my_dict:
    print("Yes, 'name' is in the dictionary.")
else:
    print("No, 'name' is not in the dictionary.")
