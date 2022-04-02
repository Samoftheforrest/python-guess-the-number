from numpy import random

def set_random_number():
    random_number = random.randint(100) + 1

    return random_number


def guess_number(num):
    guess = input('Your guess: ')

    try:
        valid_guess = int(guess)
        if valid_guess < num:
            print('Too low!')
            guess_number(num)
        elif valid_guess > num:
            print('Too high!')
            guess_number(num)
        else:
            print(f'\nWell done! You guessed the correct number!')
    except ValueError:
        print('Invalid number, please try again!')
        guess_number(num)


def play_again():
    user_input = input('Would you like to play again? y/n ')

    try:
        if user_input == 'y':
            start_new_round()
        elif user_input == 'n':
            print('Thank you for playing!')
            quit()
    except:
        print('Invalid answer')


def start_new_round():
    set_random_number()
    random_number = set_random_number()
    guess_number(random_number)
    play_again()

def main():
    print('Welcome to my \'guess the number\' game - can you guess the number between 1 and 100?')
    start_new_round()

main()