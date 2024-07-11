'''
---------------------Dice Roll Generator--------------------
'''

import random
import os

def num_die():
    while True:
        try:
            num_dice = input('Number of dice(Choose from 1 or 2):  ')
            valid_responses = ['1', '2']
            if num_dice not in valid_responses:
                raise ValueError('Enter 1 or 2 only!')
            else:
                return num_dice
        except ValueError as err:
            print(err)

def roll_dice():
    play = 'y'
    while play.lower() =='y':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_die()

        if amount == '1':
            print('Rolling the dice...')
            dice1 =  random.randint(1,6)
            print(f'The value is: {dice1}')

            play = input('Roll Again? Y/N: ')

        else:
            print('Rolling the dice...')
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print(f'The values are:')
            print(f'Dice One: {dice1}')
            print(f'Dice Two: {dice2}')
            print(f'Total: {dice1 + dice2}')

            play = input('Roll Again? Y/N: ')

    print('\nOkay! Thanks for playing! \n')

if __name__ == '__main__':
    roll_dice()