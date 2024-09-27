'''PassTutor

Password Tutor - A tool for remembering passwords... Using your mind :)

:Authors:
    @kor3n
:Version: 1.1.1
:Date: 27/09/2024
'''
# Standard Imports
import os
import time
import getpass

# 3rd Party Imports
from dotenv import load_dotenv, find_dotenv

__version__ = '1.1.1'

BANNER: str = f'''
 _____           _______    _
|  __ \         |__   __|  | |
| |__) |_ _ ___ ___| |_   _| |_ ___  _ __
|  ___/ _` / __/ __| | | | | __/ _ \| '__|
| |  | (_| \__ \__ \ | |_| | || (_) | |
|_|   \__,_|___/___/_|\__,_|\__\___/|_|
[+]Version {__version__}                   @kor3n
'''

MENU: str = '''
  1 => Set Password
  2 => Look at password
  3 => Try password

  S => Stats
  Q => Quit
'''


def password_look(pass_word: str, look_time: float) -> None:
    '''Password Look Function

    Displays the password in plain text on the terminal for specified time.

    Args:
        pass_word (str): A string of your password.
        look_time (float): Number of seconds you get to look at the password.
    '''
    clear_screen(display_banner=True)
    print(f'[!] - You have {look_time} seconds currently set to look at the password.')
    time.sleep(1)
    print(f'\n    {pass_word}    \n')
    time.sleep(look_time)
    clear_screen(display_banner=True)


def call_password(attempt_mode: bool = False, current_password: str = '') -> str | bool:
    '''Call Password Function

    Calls the user to input the password, can run in set or attempt mode.

    Args:
        attempt_mode (bool): Turns attempt mode on to attempt. Default = False
        current_password (str): The password to be checked against user intput. Default = ""
    Returns:
        str|bool: Returns the password by default, in attempt mdoe it returns a bool.
    '''
    clear_screen(display_banner=True)
    if attempt_mode:
        if getpass.getpass('    > ') == current_password:
            return True
        else:
            return False
    return getpass.getpass('    > ')


def clear_screen(display_banner: bool = False) -> None:
    '''Clear Screen Function

    Clears the terminal screen via `clear`.

    Args:
        display_banner (bool): Do you want to show the banner after the clear.
    '''
    os.system('clear')
    if display_banner:
        print(BANNER)


def main() -> None:
    '''Main Function

    This is the main function that calls other required functions to complete the script.
    '''
    clear_screen(display_banner=True)

    # Load settings
    look_timer: int = int(os.getenv('LOOK_TIME'))
    incorrect_counter: int = 0
    correct_counter: int = 0
    current_password: str = ''

    try:
        while True:
            print(MENU)
            user_intput: str = str(input('    > ')).lower()
            if user_intput == 'q':
                exit()
            elif user_intput == 's':
                clear_screen(display_banner=True)
                print(f'Correct: {correct_counter}, Incorrect: {incorrect_counter}')
            elif user_intput == '1':
                current_password = call_password()
                clear_screen(display_banner=True)
                print('   [!] - Password Set')
            elif user_intput == '2':
                password_look(current_password, look_timer)
            elif user_intput == '3':
                if call_password(attempt_mode=True, current_password=current_password):
                    correct_counter += 1
                else:
                    incorrect_counter += 1
                clear_screen(display_banner=True)
            else:
                clear_screen(display_banner=True)

    except KeyboardInterrupt as _:
        exit()


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    main()
