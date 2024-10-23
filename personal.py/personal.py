def play_game():
    print('\nThe Mysterious Cave')
    print('You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears. You have no memory of how you got here.')
    print('\nAs you get up and dust yourself off, you notice two paths ahead:')
    print('1. To your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.')
    print('2. To your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers echoing from within.')

    choice=input('\nWhich path do you choose? (type left or right): ')

    if choice == 'left':
        print('\nYou follow the dark tunnel...')
        print('You slip into a deep pit.')
        print(('Ending 1: Game Over'))
    elif choice == 'right':
        print('\nYou follow the wider and lighted path...')
        print('You see silouettes of people down the tunnel')
        print('You find a cave exit and other people!')
    else:
        print("Invalid choice. Please type 'left' or 'right'")

    print('\nYou see all of them injured by a river in the middle of the woods.')
    print('You are debating whether or not to interact with them.')
    print('1. You could either talk to them.')
    print('2. You could wander off on your own.' )

    choice_2=input('\nWhat do you choose to do? (type talk or leave):')

    if choice_2 == 'talk':
         print('\nYou go up to the injured people...')

    
print('Welcome to Text-Based Adventure Game!')
play_game()