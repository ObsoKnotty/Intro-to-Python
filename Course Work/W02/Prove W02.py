#Receipt generator

#I decided to ad a promt asking if a tip wanted to be added and then calcualed
# the new total depending on the percent they wanted to tip.

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_amount = float(input('How many children are there? '))
adult_amount = float(input('How many adults are there? '))
subtotal = ((child_meal * child_amount)+ (adult_amount * adult_meal))

print(f'\nSubtotal: ${"%.2f" % subtotal}')

tax = float(input('\nWhat is the sales tax rate? '))
sales_tax = (subtotal * (tax/100))
total = (subtotal + sales_tax)
print(f'Sales tax: ${"%.2f" % sales_tax}')
print(f'Total: ${"%.2f" % total}')


print('\nPlease answer yes or no.\n')
tip = input('Would you like to leave a tip yes/no? ')
if tip == 'yes':
    tip_percent = (float(input('What percentage would you like to tip? ')))
    tip_amount = (total * (tip_percent/100))
    tip_total = (tip_amount + total)
    print(f'Total including tip: ${"%.2f" % tip_total}')
    payment = float(input('\nWhat is the payment amount? '))
    change = (payment - tip_total)
    print(f'Change: ${"%.2f" % change}')
elif tip == 'no':
    payment = float(input('\nWhat is the payment amount? '))
    change = (payment - total)
    print(f'Change: ${"%.2f" % change}')

