import random
from os import system, name

hands = [
""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""  
    _______
---'   ____)_____
           ______)
          _______)
         _______)
---.__________)
""",
""" 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

options = ['piedra', 'papel', 'tijera']

def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def choose_options():
    user_option = int(input('Seleccione una opción 1-Piedra, 2-Papel, 3-Tijera: '))
    computer_option = random.choice(options)
    assert user_option != int, "Solo se permiten los números 1, 2 o 3"
    if user_option > 3 or user_option < 1:
        print('Esa opción no es válida')

        condition = True
        while condition:
            user_option = int(input('Seleccione una opción 1-Piedra, 2-Papel, 3-Tijera: '))
            if user_option < 4 and user_option >= 1:
                condition = False
    clearConsole()
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if ((options[user_option-1] == 'piedra' and computer_option == 'tijera') or (options[user_option-1] == 'papel' and computer_option == 'piedra') or (options[user_option-1] == 'tijera' and computer_option == 'papel')):
        print(f"Usted eligió: {hands[user_option-1]} - la computador eligió: {computer_option}")
        print('Usted ganó!')
        print('-'*20)
        user_wins += 1
    elif(options[user_option-1] == computer_option):
        print(f"Usted eligió: {hands[user_option-1]} - la computador eligió: {computer_option}")
        print('Empate')
        print('-'*20)
    else:
        print(f"Usted eligió: {hands[user_option-1]} - la computador eligió: {computer_option}")
        print('Usted perdió')
        print('-'*20)
        computer_wins += 1
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 0

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        rounds += 1
        if computer_wins == 3:
            print('La computadora ha ganado, Intenta nuevamente')
            break

        if user_wins == 3:
            print('BOOOO HAS GANADOOOOO. FELICITACIONES')
            break
    

if __name__ == '__main__':
    run_game()

