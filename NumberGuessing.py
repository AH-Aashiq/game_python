import random
from colorama import Fore

print(Fore.GREEN + ''' 
   Alachi Presents
--------------''' + Fore.RED + '''  
 ▄████ █    ██▓█████  ██████  ██████ ██▓███▄    █  ▄████      ▄████ ▄▄▄      ███▄ ▄███▓█████ 
 ██▒ ▀█▒██  ▓██▓█   ▀▒██    ▒▒██    ▒▓██▒██ ▀█   █ ██▒ ▀█▒    ██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀ 
▒██░▄▄▄▓██  ▒██▒███  ░ ▓██▄  ░ ▓██▄  ▒██▓██  ▀█ ██▒██░▄▄▄░   ▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███   
░▓█  ██▓▓█  ░██▒▓█  ▄  ▒   ██▒ ▒   ██░██▓██▒  ▐▌██░▓█  ██▓   ░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄ 
░▒▓███▀▒▒█████▓░▒████▒██████▒▒██████▒░██▒██░   ▓██░▒▓███▀▒   ░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒
 ░▒   ▒░▒▓▒ ▒ ▒░░ ▒░ ▒ ▒▓▒ ▒ ▒ ▒▓▒ ▒ ░▓ ░ ▒░   ▒ ▒ ░▒   ▒     ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░
  ░   ░░░▒░ ░ ░ ░ ░  ░ ░▒  ░ ░ ░▒  ░ ░▒ ░ ░░   ░ ▒░ ░   ░      ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░
░ ░   ░ ░░░ ░ ░   ░  ░  ░  ░ ░  ░  ░  ▒ ░  ░   ░ ░░ ░   ░    ░ ░   ░  ░   ▒  ░      ░     ░   
      ░   ░       ░  ░     ░       ░  ░          ░      ░          ░      ░  ░      ░     ░  ░
                                                                 ''' + Fore.WHITE + ''' Created by Alachi
        ''')
print("")

def guess(x):
     random_number = random.randint(1,x)
     guess = 0
     while guess != random_number:
          guess = int(input(Fore.YELLOW +f'Guess a number between 1 and {x}: '))
          if guess < random_number:
               print(Fore.RED +'Sorry guess again. Too low.')
          elif guess > random_number:
               print(Fore.RED +'Sorry, guess again. Too high.')
     print(Fore.CYAN +f"Yay, congratulations. You have guess the number {random_number} correctly!!.")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(Fore.YELLOW + f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(Fore.CYAN + f'Yay! The computer guessed your number, {guess}, correctly!')


#for guess number
guess(10)

#computer gussing
# computer_guess(10) 





