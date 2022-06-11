import random
repeat = True
while repeat:
    choices = ['r', 'p', 's']
    cpu = random.choice(choices)
    
    input_check = True
    while input_check:
        player = input("Pick an option from r, p, s:\n").lower()
        if player == cpu:
            print(cpu)
            print("It's a tie")
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
            print("Wrong input, try again")

    play_again = input("Do you want to play again? y/n\n").lower()

    if play_again == "y":
        repeat = True
    elif play_again == "n":
        repeat = False
