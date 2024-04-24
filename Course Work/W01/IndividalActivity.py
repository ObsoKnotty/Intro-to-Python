first = input('What is your first name? ')
last = input('What is your last name? ')
email = input('What is your email address? ')
phone = input('What is your phone number? ')
job = input('What is your job title? ')
idNum = input('What is your ID number? ')
hair = input('What is your hair color? ')
eyes = input('What is your eye color? ')
month = input('Please enter the month you were born ')
training = input('Have you received formal training? ')

print('\nThe ID Card is:')
print('---------------------------------')
#THis is the first way I did it, I need to remmeber I can split this up into multiple prints
print(f"{last.upper()}, {first.title()}\n{job.title()}\nID: {idNum}\n\n{email.lower()}\n{phone}\n\nHair: {hair:12} Eyes: {eyes}\nMonth: {month:11} Training: {training}")
print('---------------------------------')


#this is the sample solution: the sample is much easier to read as the prints are seperate and short.

# print("Please enter the following information:")

# print()

# # Ask for the basic information
# first = input("First name: ")
# last = input("Last name: ")
# email = input("Email address: ")
# phone = input("Phone number: ")
# job_title = input("Job title: ")
# id_number = input("ID Number: ")

# # Ask for the additional information
# hair_color = input("Hair color: ")
# eye_color = input("Eye color: ")
# month = input("Starting Month: ")
# training = input("Completed additional training? ")

# # Now print out the ID Card
# print("\nThe ID Card is:")
# print("----------------------------------------")
# print(f"{last.upper()}, {first.capitalize()}")
# print(job_title.title())
# print(f"ID: {id_number}")
# print()
# print(email.lower())
# print(phone)
# print()

# # There are various ways to accomplish the spacing

# # In this approach, I told it that hair_color will take exactly 15
# # spaces, and month will take 14. That way, the next columns will
# # line up. I had to do month 14 (instead of 15) because the word
# # 'Month' that came before my value was one letter longer.

# print(f"Hair: {hair_color:15} Eyes: {eye_color}")
# print(f"Month: {month:14} Training: {training}")
# print("----------------------------------------")