import random   


user_choices = ['R', 'P', 'S']
computer_choices = ['Rock', 'Paper', 'Scissors']

while True:
    print('lets play Rock,Paper,Scissors ......')
    print('Pick your option: \n> "R" for "rock" \n> "P" for "paper" \n> "S" for "scissors" \n> "Q" to quit')
    choice = input(' \n> Choice: ')

    if (choice.upper() not in user_choices and choice.upper() != "Q"):
        print('{} is a wrong option, please enter a correct option'.format(choice))
        if (choice.upper() == 'Q'):
            print('Bye')
            break
    else:
        break

cpu_choice = random.choice(computer_choices)

u_choice = choice.split()

if choice.upper() == "R":
    u_choice.append('ock')
elif choice.upper() == "P":
    u_choice.append('aper')
elif choice.upper() == "S":
    u_choice.append('cissors')

user_choice = ("").join(u_choice).title()

print("\nPlayer ({}) : CPU ({})".format(user_choice, cpu_choice))

while True:
    if (user_choice == cpu_choice):
        print("It's a tie. Restarting game...")

        while True:
            print('lets play Rock,Paper,Scissors ......')
            print('Pick your option: \n> "R" for "rock" \n> "P" for "paper" \n> "S" for "scissors" \n> "Q" to quit')
            choice = input('Choice: ')

            if (choice.upper() not in user_choices and choice.upper() != "Q"):
                print('you have entered a wrong option, please enter a correct option')
            else:
                break

        cpu_choice = random.choice(computer_choices)

        u_choice = choice.split()

        if choice.upper() == "R":
            u_choice.append('ock')
        elif choice.upper() == "P":
            u_choice.append('aper')
        elif choice.upper() == "S":
            u_choice.append('cissors')

        user_choice = ("").join(u_choice).title()

        print("\nPlayer ({}) : CPU ({})".format(user_choice, cpu_choice))
    
    else: 
        break

if user_choice == "Rock" and cpu_choice == "Paper":
    print("Uh-oh! Paper covers Rock, Computer wins!")
elif user_choice == "Paper" and cpu_choice == "Rock":
    print("Yay! Paper covers Rock, You win!")
elif user_choice == "Rock" and cpu_choice == "Scissors":
    print("Yay! Rock blunts Scissors, You win!")
elif user_choice == "Scissors" and cpu_choice == "Rock":
    print("Uh-oh! Rock blunts Scissors, Computer wins!")
elif user_choice == "Paper" and cpu_choice == "Scissors":
    print("Uh-oh! Scissors cuts Paper, Computer wins!")
elif user_choice == "Scissors" and cpu_choice == "Paper":
    print("Yay! Scissors cuts Paper, You win!")
elif choice.upper() == 'Q':
    print("computer chose {}, maybe you would have won........want to play?".format(cpu_choice))
else:
    print("something went wrong")





# print(random.choice(list))