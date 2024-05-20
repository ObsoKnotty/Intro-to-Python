#Adventure Game

#I am adding a while loop to make sure that the user only makes valid inputs

while(True):
    try:

        main_branch = input('You wake up and find yourself in a mysterious land. You can see a CASTLE to your left and a TOWN to your right. Where do you want to go? ').lower()
        
        if main_branch == 'castle':
            castle_branch = input('You walk towards the castle, and on your way you see a group of men with swords walking towards you. Do you want to HIDE or SPEAK with them? ').lower()
            if castle_branch == 'hide':
                hide_branch = input('You run into the forest on the side of trail. As the men pass you can see they were escorting a hooded figure on a horse. Do you FOLLOW or continue to the CASTLE? ').lower()
                if hide_branch == 'follow':
                    print('You attempt to follow the escort from behind but the guards realise you are chasing after them. They quickly chase after you and arrest you.')
                    break
                elif hide_branch == 'castle':
                    print('You eventually arrive at the castle only to be told you have to leave because the lord of tha castle just left home.')
                    break
                else:
                    raise ValueError
                
            elif castle_branch == 'speak':
                cas_speak_branch = input('You walk up to the men and they ask you to halt and ask you to leave, you can see a hooded figure on a horse behind them. Do you LEAVE or do you CONTINUE? ').lower()
                if cas_speak_branch == 'leave':
                    print('You apologize for the trouble and turn to leave, then the hooded figure asks you to wait and come speak with them. He introduces himself as the duke of the land and ask you to accompany him on the trip')
                    break
                elif cas_speak_branch == 'continue':
                    print('As you walk forward the men pull out there swords and tell you, you are under arrest and they tie you up')
                    break
                else:
                    raise ValueError
            else:
                raise ValueError

        elif main_branch == 'town':
            town_branch = input('You walk towards the town and see that there are guards at the gates. Do you wish to SNEAK in or SPEAK with the guards? ').lower()
            if town_branch == 'sneak':
                sneak_branch = input('You walk around the outside of the town and see a WALL you could climb, or a SEWER you could crawl into. Which do you choose? ').lower()
                if sneak_branch == 'wall':
                    print('You climb up the wall but as you get to the top you hand slips and you hit the ground with a large thud. The guards hear this and come to take you away and through you in the dungeon')
                    break
                elif sneak_branch == 'sewer':
                    print('You crawl through the smelly and dirty sewer eventually finding an opening overhead. As you exit you find yourself coming out of the toilet in a tavern.')
                    break
                else:
                    raise ValueError
                
            elif town_branch == 'speak':
                town_speak_branch = input('You walk up to the guard and he asks what your buisness in town is. You think to either say it is to REST and find something to eat, or you can say you are LOST. What do you choose? ').lower()
                if town_speak_branch == 'rest':
                    print('The guard lets you through and recommend his favorite tavern that is close by for you to stay at.')
                    break
                elif town_speak_branch == 'lost':
                    print('The guard tells you to follow his colligue as they take you to the barracks so they can help you find out where you are.')
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print('\nRESETTING')
        print('\nPlease input one of the words in BOLD\n')