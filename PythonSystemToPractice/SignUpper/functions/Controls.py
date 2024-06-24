from colorama import Fore

peoples = []

def view_peoples():
    if len(peoples) == 0:
        print(Fore.RED + '-' * 30)
        print(Fore.RED + 'Nothing here. :[')
        print(Fore.RED + '-' * 30)
    else:
        print(Fore.GREEN + '-' * 30)
        for i, it in enumerate(peoples):
            print(f'{i+1} - ' + Fore.GREEN + f'{it}')
        print(Fore.GREEN + '-' * 30)

        
def new_person():
    print(Fore.GREEN + '-' * 30)
    is_good = False
    while is_good is False:
        name = input(Fore.WHITE + 'Name: ')
        
        if not name == '':
            is_good = True
        else:
            print(Fore.RED + 'ERROR - unknown value')
            print()
        
    peoples.append(name)
    print(Fore.GREEN + f'Added {name} in list :]')
    print(Fore.GREEN + '-' * 30)    
    