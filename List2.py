# Generating a list of squares using list comprehension
squares = [x**2 for x in range(1, 6)]

print("List of Squares:", squares)

# Filtering even numbers using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)

# Creating a list of lengths of words in a sentence
sentence = "This is a sample sentence for list comprehension"
word_lengths = [len(word) for word in sentence.split()]

print("Word Lengths:", word_lengths)

# Combining elements from two lists using zip and list comprehension
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

name_age_pairs = [(name, age) for name, age in zip(names, ages)]

print("Name-Age Pairs:", name_age_pairs)
