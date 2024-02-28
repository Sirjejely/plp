"""Write a program that accepts user input
to create a list of integers. Then,compute the
sum of all the integers in the list."""

#take the numbers as a string first separated by spaces
scoresStrings=input('Enter your scores separated by a spaces: ')
#the next thing is to convert from string to integers
scoresInt=[int(x) for x in scoresStrings.split()]
# Add the scores
scoreSum = sum(scoresInt)
print(f'the list of scores: {scoresInt}')
print(f'The sum of scores is: {scoreSum}')

"""Create a tuple containing the names of five of your favorite books.
Then, use a for loop to print each book name on a separate line."""

books=('Bible','physic_bks','math_bks','hist_bks','comm_bks')
for book in books:
    print(book)

"""Write a program that uses a dictionary to store information about a
person, such as their name, age, and favorite color. Ask the user for input
and store the information in the dictionary.Then, print the dictionary to
the console"""
# Create an empty dictionary to store person information
person_info = {}
# Ask the user for input
person_info['name'] = input("Enter the person's name: ")
person_info['age'] = input("Enter the person's age: ")
person_info['favorite_color'] = input("Enter the person's favorite color: ")
# Print the dictionary to the console
print("\nPerson Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")
#OR we can do it like this:
# Ask the user for input and create the dictionary
person_info = {
    'name': input("Enter the person's name: "),
    'age': input("Enter the person's age: "),
    'favorite_color': input("Enter the person's favorite color: "),
}

# Print the dictionary to the console
print("\nPerson Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")

"""Write a program that accepts user input to create two sets of integers.
Then, create a new set that contains only the elements that are common
to both sets."""
# write two sets A and B to accept sets of integers spaced.
A = input('Enter set of intergers separated in space: ')
B = input('Enter set of intergers separated in space: ')
A_set = set(A)
B_set = set(B)
print('The common element between set A and set B is: ', A_set.intersection(B_set))
