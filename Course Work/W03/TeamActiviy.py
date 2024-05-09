#Grade Calculator Program
grade_percent = (float(input('What percentage did you receive? ')))

if grade_percent >= 90:
    grade = 'A'   
elif grade_percent >= 80:
    grade = 'B'  
elif grade_percent >= 70:
    grade = 'C'
elif grade_percent >= 60:
    grade = 'D'
else:
    grade = 'F'

last_digit = grade_percent % 10

if last_digit >= 7:
    grade_symbol = "+"
elif last_digit < 3:
    grade_symbol = "-"
else:
    grade_symbol = ""

if grade_percent >= 93:
    grade_symbol = ""

if grade == 'F':
    grade_symbol = ''






print(f'Your letter grade is {grade}{grade_symbol}')
    

if grade_percent >= 70:
    print('Great Job! You passed!')
else: 
    print("You didn't pass, but study hard and try again!")