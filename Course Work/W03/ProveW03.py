#Adventure Game

#I am adding a while loop to make sure that the user only makes valid inputs

while(True):
    try:
        main_branch = input('You wake up and find yourself in a mysterious land. You can see a CASTLE to your left and a TOWN to your right. Where do you want to go? ').lower()
        
        if main_branch == 'castle':
            print('\nON TO THE FIRST PATH')
            break

        elif main_branch == 'town':
            print('\nON TO THE SECOND PATH')
            break
        else:
            raise ValueError

    except ValueError:
        print('\nPlease input one of the words in BOLD\n')