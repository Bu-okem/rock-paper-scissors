# option = ['r', 'p', 's']

# choice = input("Pick one:\n R for rock\n P for paper\n S for scissors\n")

# if choice == 'r':
#     pass

import random
while True:
    choices = ['r', 'p', 's']
    cpu = random.choice(choices)
    player = input("Pick an option from r, p, s:\n").lower()
    if player == cpu:
        print(cpu)
        print("It's a tie")
        break
    elif player == 'r' and cpu == 'p':
        print(cpu)
        print('You lose')
        break
    elif player == 'r' and cpu == 's':
        print(cpu)
        print('You win')
        break
    elif player == 'p' and cpu == 'r':
        print(cpu)
        print('You win')
        break
    elif player == 'p' and cpu == 's':
        print(cpu)
        print('You lose')
        break
    elif player == 's' and cpu == 'p':
        print(cpu)
        print('You win')
        break
    elif player == 's' and cpu == 'r':
        print(cpu)
        print('You lose')
        break
    else:
        pass