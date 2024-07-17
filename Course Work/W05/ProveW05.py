#Shopping cart


print( 'Welcome to  your Shopping Cart!')

cart = []

while(True):
    try:  

        print('\nPlease select one of the following: \n 1. Add Item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')

        selected = int(input('Please enter your selection: '))

        if selected in range(1, 6):
            if selected == 1:
                item = input('What item would you like to add? ').capitalize()
                item_price = float(input(f'What is the price of {item}? '))
                added_item = [item, item_price]
                cart.append(added_item)
                print(f"'{item}' has been added to your cart")

            elif selected == 2:
                print('The contents in your shopping cart are:')
                index = 1
                for i in cart:
                    contents = '{stuff} - ${price:.2f}'
                    print(str(index)+'.'+ ' ' + contents.format(stuff = i[0], price = i[1]))
                    index += 1

            elif selected == 3:
                remove = int(input('Which item would you like to remove? ')) - 1
                del cart[remove]
                print('Item removed.')
            
            elif selected == 4:
                total = 0
                for i in cart:
                    total += i[1]
                print(f'The total price of the items in your shopping cart is ${total:.2f}'.format(total))

            elif selected == 5:
                print('Thank you. Goodbye.')
                break
        else:
            raise ValueError

    except ValueError:
        print('\nERROR')
        print('Please select a correct input (1 - 5)\n')