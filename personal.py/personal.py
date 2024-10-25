def play_game():
    print('\nThe Mysterious Cave')
    print('You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears. You have no memory of how you got here.')
    print('\nAs you get up and dust yourself off, you notice two paths ahead:')
    print('1. To your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.')
    print('2. To your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers echoing from within.')

    while True:
        choice_1=input('\nWhich path will you take?(Enter 1 for left. Enter 2 for right):')
        
        if choice_1=='1':
            print('\nYou follow the dark tunnel...')
            print('You here the sound of rushing water get louder as you go further in. You notice:')
            print('\n1.A wooden bridge crossing a river below.')
            print('2.Some old mining equipment and a functional flashlight.')
            print('\nPossible commands:')
            print('Cross')
            print('Examine')

            while True:
                action1=input('\nWhat do you do?(Enter Cross or Examine):')

                if action1 == 'Cross':
                    print('\nYou step foot on the wooden bridge...')
                    print('The bridge is creaking as you having difficulty keeping balance.')
                    print('As you are crossing, the bridge snaps and you fall into the river.')
                    print('GAME OVER')
                    break

                elif action1 =='Examine':
                    print('\nYou make your way to the flashlight and equipment...')
                    print('You turn on the flashlight to see a treasure chest. You open it.')
                    print('You find an ancient treasure map!')
                    print('\nThe map shows are 2 possible routes:')
                    print('1.Follow the flow of the river through the edge of the cliff you are on.')
                    print('2.Go back to where you originally started.')

                    while True:
                        choice3=input('\nWhat instruction do you take?(Enter 1 or 2):')

                        if choice3=='1':
                            print('\nYou follow the river...')
                            print('You see stairs that lead you down into the river. Down the river you see light.')
                            print('You see a boat that could take down the river and a crystal cavern the opposite way.')
                            print('\nThere are two commands.')
                            print('1. Go down the river and sail into light.')
                            print('2. Go towards the crystal cavern to mine with the equipment.')

                            while True:
                                action2=input("\nWhat do you decide to do?(Enter 'Flee' or 'Go away'):")
                                
                                if action2=='Flee':
                                    print('\nYou hop on the boat and start sailing down the river...')
                                    print('The light becomes brighter.')
                                    print('\nYou found a cave exit!')
                                    print('1. To your left there is a village.')
                                    print('2. To your right there is a jungle.')

                                    while True:
                                        choice5=input('\nWhich way do you go?(Enter 1 or 2):')

                                        if choice5=='1':
                                            print('\nYou make your way to the village...')
                                            print('You are approached by a group of people.')
                                            print('They are unfriendly and attack you.')
                                            print('GAME OVER')
                                            break
                                        
                                        elif choice5=='2':
                                            print('\nYou make your way towards the jungle...')
                                            print('You are starting to get hungry.')
                                            print('\nYou come across bushes of berries!')
                                            print('1. Eat some?')
                                            print('2. Leave them.')

                                            while True:
                                                choice6=input('\nWhat do you do?(Enter 1 or 2):')

                                                if choice6=='1':
                                                    print('\nYou eat the berries...')
                                                    print('You gain health and stamina to get through the woods!')
                                                    print('You encounter tribal people who are welcoming.')
                                                    print('They take care of you and provide a place to stay.')
                                                    print('You are safe.')
                                                    print('GAME WON')
                                                    break
                                                elif choice6=='2':
                                                    print('\nYou leave the berries behind...')
                                                    print('You have no stamina or health left to get through the woods.')
                                                    print('GAME OVER')
                                                    break
                                                else:
                                                    print('\nInvalid choice. Please enter 1 or 2.')
                                            break
                                        else:
                                            print('\nInvalid choice. Please enter 1 or 2.')
                                    break
                                elif action2=='Go away':
                                    print('\nYou go towards the crystal cavern to mine...')
                                    print('You start mining.')
                                    print('You start getting tired and hungry')
                                    print('You become to exhausted to keep mining.')
                                    print('GAME OVER')
                                    break
                                else:
                                    print('\nInvalid choice. Please enetr 1 or 2.')
                            break
                        elif choice3=='2':
                            print('\nYou go back to where you orignally started...')
                            print('You make your way back into the dark passage.')
                            print('Its is so dark you cannot see anything head.')
                            print('You slip and fall into a pit.')
                            print('GAME OVER')
                            break
                        else:
                            print('\nInvalid choice. Please eneter 1 or 2.')
                    break
                        
                else:
                    print("\nInvalid choice. Please eneter 'Cross' or 'Examine'.")
            break
    
        elif choice_1=='2':
            print('\nYou follow the wide path into the mysterious light...')
            print('The whispers grow louder and the light in becoming brighter.You find yourself in a chamber with:')
            print('\n1. An alter with symbols.')
            print('2. A spiral staircase that leads upward.')
        
            while True:
                choice7=input('\nWhat do you do?(Enter 1 or 2):')

                if choice7=='1':
                    print('\nYou approach the alter...')
                    print('A magical portal opens up.')
                    print('You enter the portal that leads you to an unknown location stuck forever.')
                    print('GAME OVER')
                    break
                elif choice7=='2':
                    print('\nYou make your way up the stairs...')
                    print('You hear the whispers grow louder.')
                    print('You find a group of gnomes!')
                    print('\nThey ask you to join their group.')
                    print('1. You join them.')
                    print('2. You continue to go up the stairs.')

                    while True:
                        choice8=input('\nWhat do you choose?(Enter 1 or 2):')

                        if choice8=='1':
                            print('\nYou join their group...')
                            print('They lead you into an unknown room.')
                            print('They betray you.')
                            print('GAME OVER')
                            break
                        elif choice8=='2':
                            print('\nYou leave them and continue to go up the stairs...')
                            print('As you go up, you find an unknown room.')
                            print('It is an abandoned library!')
                            print('You search through the books.')
                            print('You find one that shows you a way out of the chamber!')
                            print('\nThe book gives you two options.')
                            print('1. Flip a switch to the right.')
                            print('2. Go to the back of the library to find a key.')

                            while True:
                                choice9=input('\nWhat instruction to you take?(Enter 1 or 2):')

                                if choice9=='1':
                                    print('\nYou flip the switch...')
                                    print('The wall flips, leading to an exit to the cave!')
                                    print('Outside, You are in a city.')
                                    print('\nYou want to go across the street but there are too many cars passing.')
                                    print('1. Do you try to get across the street?')
                                    print('2. Do you stay along the sidewalk and find somewhere to recover.')

                                    while True:
                                        choice10=input('\nWhat do you do?(Enter 1 or 2):')

                                        if choice10=='1':
                                            print('\nYou cross the street...')
                                            print('As soon as you step foot onto the road, a car runs over you.')
                                            print('GAME OVER')
                                            break
                                        elif choice10=='2':
                                            print('\nYou stay along the sidewalk...')
                                            print('You encounter a bridge that takes you across the street. Patience is key.')
                                            print('\nWhen you cross the street. You can go into two buildings.')
                                            print('1. A shrine')
                                            print('2. A restaurant')

                                            while True:
                                                choice11=input('\nWhere do you go?(Enter 1 or 2):')

                                                if choice11=='1':
                                                    print('\nYou enter the shrine...')
                                                    print('A group of people greet you, offering you a place to stay.')
                                                    print('You are able to rest and eat as they adopt you into their family')
                                                    print('You are safe')
                                                    print('GAME WON')
                                                    break
                                                elif choice11=='2':
                                                    print('\nYou enter the restaurant...')
                                                    print('They do not like your appearance and attack you.')
                                                    print('GAME OVER')
                                                    break
                                                else:
                                                    print('\nInvalid choice. Please eneter 1 or 2.')
                                            break

                                        else:
                                            print('\nInvalid choice. Please eneter 1 or 2.')
                                    break

                                elif choice9=='2':
                                    print('\nYou head to the back of the library...')
                                    print('You are led to a room.')
                                    print('\nYou have two choices:')
                                    print('Open door')
                                    print('Do not enter')

                                    while True:
                                        action3=input("\nWhat do you do?(Enter 'Open door' or 'Do not enter')")

                                        if action3=='Open door':
                                            print('You open the door...')
                                            print('You are greeted by a friendly genie who offers to go back home.')
                                            print('You accept.')
                                            print('He sends you to an unknown location and are lost forever.')
                                            print('GAME OVER')
                                            break

                                        elif action3=='Do not enter':
                                            print('You do not enter the room...')
                                            print('You go back to the switch and flip it.')
                                            print('The switch does nothing. It only worked when you had the option the first time.')
                                            print('You are now stuck here forever.')
                                            print('GAME OVER')
                                            break

                                        else:
                                            print("\nInvalid choice. Please enter 'Open door' or 'Do not enter.")
                                    break

                                else:
                                    print('\nInvalid choice. Please eneter 1 or 2.')
                            break
                        else:
                             print('\nInvalid choice. Please eneter 1 or 2.')
                    break    
                else:
                     print('\nInvalid choice. Please enter 1 or 2.')
            break

        else:
            print('Invalid choice. Please enter 1 or 2')
    
    while True:
        play_again=input('\nWould you like to play again?(Yes or No):')
        
        if play_again=='No':
            print('Thanks for playing! GAME OVER')
            break
        elif play_again=='Yes':
            print(play_game())
            break
        else:
            print("Invalid choice. Please enter 'Yes' or 'No'")

print('Welcome to Text-Based Adventure Game!')
play_game()