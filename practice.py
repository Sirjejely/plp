a, b, c = 5 , 3.2, 'Hello'
print(a)
print(b)
print(c)
num=5
Num=45
print(num)
print(Num)
#We use index numbers which start from 0 to print items from list.
Languages=['Igbo','Hausa','Yoruba']
print(Languages[0])
print(type(Languages))
#it is also use to asses items in tuple too.
Foods=('garri','cassave','ewa', 'agbada')
print(Foods[2]) #ewa
print(type(Foods))
#Strings are words and and always with"" or ''. a number in those quotation mark is also seen as strings.
message='I love python language'
print(message)
student_id={112,114,116,115,121}
print(type(student_id))
print(student_id)
Capital_city={'Imo':'Owerri','Lagos':'Ikeja'}
print(type(Capital_city))
print(Capital_city)
print(Capital_city['Imo'])
num1=6
num2=7
print('This is output')

# print has 5 parameters
#print(object= separator= end= file= flush=)
print('Good morning!')
print('It is rainy today')#The output will show in two lines
print('Good morning!',end='')
print('It is rainy today') #the outputr will be in a line
print('Good morning!')
print('New Year',2024, 'See you soon!', sep='. ')#This separates all the print with the . specified
number=-13.4
name="Unical"
print(5)#literal
print(number)#variables
print(name)
print('Good morning!')
print('PowerLP is ' + ' awesome.')#This concatenate the strings.
#output formatting
x=5
y=17
print('the value of x is {} and y is {}'.format(x,y))
#The curling braces are used for placeholders.
#Python input: Asking users for input
num=input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))
#The above gave a string, to make it a int or float we asked for the input as:
num=int(input('Enter a number: '))
print('You Entered:', num)
print('Data type of num:', type(num))
a = (1, 2, 3)
b = list(a)
print(b)
x={}
x[2]=10
x[1]=[20,30,40]
print(x[1][2])
