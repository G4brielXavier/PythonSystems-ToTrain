from colorama import Fore
from functions.Controls import view_peoples, new_person

options = ['View all peoples', 'New person', 'Leave']

def gen_menu():
    print()
    print(Fore.CYAN + "Main Menu")
    print()
    for i, it in enumerate(options):
        print(Fore.CYAN + f'{i+1}' + Fore.GREEN + f' - {it}')
    print()
    
def chosse_option():
    is_good = False
    while is_good is False:
        try:
            value = int(input(Fore.WHITE + "Chosse a option: "))
        except ValueError:
            print(Fore.RED + f'ERROR - unknown value')
            print()
        else:
            if value <= 3:
                is_good = True       
    
    return value

def verify_option(value):
    if value == 1:
        view_peoples()
        option_configured()
    elif value == 2:
        new_person()
        option_configured()
    elif value == 3:
        print()
        print(Fore.CYAN + 'Ok, Thank you! :]')
        print()
                   
def option_configured():
    gen_menu()
    value = chosse_option()
    verify_option(value)
    
