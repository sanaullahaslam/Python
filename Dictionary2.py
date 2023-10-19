# Creating a nested dictionary
student = {
    'name': 'Alice',
    'age': 20,
    'grades': {
        'math': 90,
        'history': 85,
        'english': 95
    }
}

# Accessing elements in the nested dictionary
print("Student Name:", student['name'])
print("Math Grade:", student['grades']['math'])

# Modifying grades
student['grades']['history'] = 88
print("Updated grades:", student['grades'])

# Adding a new subject and grade
student['grades']['science'] = 92
print("Grades after adding Science:", student['grades'])

# Iterating through the nested dictionary
print("Subject-wise Grades:")
for subject, grade in student['grades'].items():
    print(f"{subject}: {grade}")

# Checking if a key exists in the nested dictionary
if 'age' in student:
    print("Yes, 'age' is a key in the student dictionary.")
else:
    print("No, 'age' is not a key in the student dictionary.")
