# Wind chill formula: 35.74 + 0.621T - 35.75(v^0.16) + 0.4275(v^0.16)
# T = Air temp in F and V = Wind Speed in Mph
v = 0

t = float(input('What is the temperature? '))

degree_type = input('Fahrenheit of Celsius (F/C)? ')


def windchill(t, v):
    return round(35.74 + (0.6215*t) - (35.75*v**0.16) + (0.4275*t*v**0.16), 2)
    

def celsius_to_fahrenheit(t): 
    return (t * 9/5) + 32



if degree_type.lower() == 'f':
    while v <60:
        v += 5
        print(f'At temperature {t}F, and wind speed {v} mph, the windchill is: {windchill(t, v)}F')

elif degree_type.lower() == 'c':
    x = celsius_to_fahrenheit(t)
    while v <60:
        v += 5
        print(f'At temperature {x}F, and wind speed {v} mph, the windchill is: {windchill(x, v)}F')

   
