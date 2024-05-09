#Find the area of shapes

import math
meter = 10000

square_length = input('What is the length of the square in centimeters? ')
square_num = ([int(i) for i in square_length.split() if i.isdigit()])
square_area = (float(square_num[0])**2)

if square_area >= meter:
    print(f'The area of the square is: {square_area / meter} square meters')
else:
    print(f'The area of the square is: {square_area} square centimeters')

rectangle_length = input('What is the length of the rectangle in centimeters? ')
rectangle_width = input('What is the width of the rectangle in centimeters? ')
rectangle_length_num = ([int(i) for i in rectangle_length.split() if i.isdigit()])
rectangle_width_num = ([int(i) for i in rectangle_width.split() if i.isdigit()])
rectangle_area = (float(rectangle_length_num[0]) * float(rectangle_width_num[0]))

if rectangle_area >= meter:
    print(f'The area of the rectangle is: {rectangle_area / meter} square meters')
else:
    print(f'The area of the rectangle is: {rectangle_area} square centimeters')

circle_radius = input('What is the radius of the circle in centimeters? ')
circle_radius_num = ([int(i) for i in circle_radius.split() if i.isdigit()])
circle_area = (math.pi * float(circle_radius_num[0])**2)

if circle_area >= meter:
    print(f'The area of the circle is : {circle_area / meter} square meters')
else:
    print(f'The area of the circle is : {circle_area} square centimeters')
