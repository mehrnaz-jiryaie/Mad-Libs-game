from menu import menu
import sys

def re_play():
    answer = input('Do you want to replay?(yes/no)')
    if answer == 'yes':
        menu()
    elif answer == 'no':
        sys.exit()