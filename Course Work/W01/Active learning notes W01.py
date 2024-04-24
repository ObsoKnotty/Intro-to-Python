                                 #ACTIVITY 1
# print('hello world')
# print()
# name = input('What is your name?  ')
# print()
# print('Hello')
# print(name)



                                #ACTIVITY 2
    #commented out incorrect print
##print('it's a small world')
#print("It's a small world")

print()

# Ctrl + K + C will auto comment a selected line
# Ctrl + K + U will undo comments of a selected line

first_name = 'Taylor'
last_name = 'Kirk'
#Combining string variables
print(first_name + last_name)
#Combining string literal with variables
print('Hello ' + first_name + ' ' + last_name)

print()

sentence = 'i have a cat'
#this will make all letters upper case
print(sentence.upper())
#this will make all letters lower case
print(sentence.lower())
#this will capitalize the first letter in the string
print(sentence.capitalize())
#this will count how many of the given input is in the string
#remember that lowercase and uppercase are two seperate values
print(sentence.count('a'))
#this will capitalize the first letter in every word in the string
print(sentence.title())

print()

#This can all be combined into a large print
surname = input('What is your first name?')
forename = input('What is your last name?')
#putting the .capitalize will make it so that no matter the user input
#the name will come out cased correctly
print('Hello '+ surname.capitalize() + ' ' + forename.capitalize())

print()

#Formatting Strings
#All of the outputs below will print the exact same thing
#bad nameing habit dont do the 1234 thing.
output1 = 'Hello, '+ first_name + ' ' + last_name
output2 = 'Hello, {} {}'.format(first_name, last_name)
output3 = 'Hello, {0} {1}'.format(first_name, last_name)
output4 = f'Hello, {first_name} {last_name}'
print(output1)
print(output2)
print(output3)
print(output4)