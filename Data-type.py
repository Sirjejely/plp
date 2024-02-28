#Data types are like our symmantics that enabbe us to do our programmimng in python
#Variable is container that contains any value in it in our computer memory
#type is an in-built variable used to know what type of variable you are dealing with
type(7.34)
type(5+3j)
print(type(7.34))
print(type(5+3j))
a=123
print("The type of variable having value", a, "is ",type(a))
b=True
print("The type of variable having value", a, "is ",type(b))
c=20.345
print("The type of variable having value", a, "is ",type(c))
d=13+3j
print("The type of variable having value", a, "is ",type(d))
#REpitation in string
str="I love You "
print(str* 4)
numbers=[number*number for number in range(1,6)]
print(numbers)
# numbers=[number*x for x in range(1,6)]
# print(numbers)
squares={1:1,3:9, 5:25, 7:49, 9:81}
print(1 in squares)
print(2 not in squares)
print(49 in squares)
for i in squares:
    print(squares[i])
#Sets can not be duplicated
vowels={'a', 'e','a', 'i', 'e','o','u','o'}
print(vowels)#see, the vowels did not repeat.
# we use add to add item to set
num={12,13,15,31}
num.add(32)
print(num)
#update() is used to update set with items from list, tuple, set, etc
companies={'Lacoste', 'Ralph Lauren'}
techcompanies=['apple', 'google', 'apple']
companies.update(techcompanies)
print(companies)
#We use discard() to remove value from set
languages={'swift','java','python'}
#languages.discard('java')# this can work as the one below
removedvalue=languages.discard('java')
print(languages)
#print(enumerate(languages))
my_set = {1, 2, 3, 4, 5}
set_as_list = list(my_set)
for index, value in enumerate(set_as_list):
    print(f"Element at index {index} is: {value}")
minimum_value = min(my_set)
maximum_value = max(my_set)
print(f"Minimum value in the set: {minimum_value}")
print(f"Maximum value in the set: {maximum_value}")
numeric_set = {10, 20, 30, 40, 50}
sum_of_elements = sum(numeric_set)
print(f"Sum of elements in the set: {sum_of_elements}")
unsorted_set = {5, 3, 1, 4, 2}
sorted_list = sorted(unsorted_set)
print(f"Sorted list from the set: {sorted_list}")
my_set = {True, True, False, True}
result_all = all(my_set)
print(f"All elements in the set are True: {result_all}")
my_set = {False, False, True, False}
result_any = any(my_set)
print(f"At least one element in the set is True: {result_any}")
even_num={2,4,6,8}
print('set: ',even_num)
print('Total Element: ',len(even_num))
A={1,3,5}
B={0,2,4}
print('Union of A and B is:',A|B)
C={2,3,6}
print('The intersection of A and C is:',A&C)
print('The intersection of A and C is:',A.intersection(C))
#Any of the two methods is used for intersection
print('Difference between A and C is:',A-C)
print('The intersection of A and C is:',A.difference(C))
#The above is difference which is what is in A that is not in C
print('The Symmetric difference of A and C is:',A.symmetric_difference(C))
print('The Symmetric difference of A and C is:',A^C)
#Symmetric differece is all that is in A and C without the common elements.
if A == C:
    print('Set A and set C are equal')
else:
    print('set A and set C are not equal')
#The == operator is used to check if two sets are equal or not.



