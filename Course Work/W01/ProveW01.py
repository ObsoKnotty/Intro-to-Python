#Madlib generator

#I decided to make verb an array to see if I could add elements to an array using the input method to get a response out of a user.
verb = []
print('Please enter the following:')
print()
adjective = input('Adjective: ')
animal = input('Animal: ')
verb.append(input('Verb: '))
exclamation = input('Exclamation: ')
verb.append(input('Verb: '))
verb.append(input('Verb: '))
print()

print('Your story is:\n')



print(f'''The other day, I was really in trouble. It all started when I saw a very
{adjective.lower()} {animal.lower()} {verb[0].lower()} down the hallway. "{exclamation.upper()}!" I yelled. But all
I could think to do was to {verb[1].lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb[2].lower()}
right in front of my family.''')