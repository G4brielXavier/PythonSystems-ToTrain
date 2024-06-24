from colorama import Fore

def readInteger():
    is_correct = False
    while is_correct is False:
        try:
            n = int(input(Fore.WHITE + "Type it a integer number: "))
        except (ValueError, NameError):
            print(Fore.RED + f'ERROR: Please, type it a valid number integer.')
        except KeyboardInterrupt:
            print(Fore.RED + f'The User not prefered type the integer number.')
            n = 0
            is_correct = True
        else:
            is_correct = True
    
    return n

def readFloat():
    is_correct = False
    while is_correct is False:
        try:
            n = float(input(Fore.WHITE + "Type it a float number: "))
        except ValueError:
            print(Fore.RED + f'ERROR: Please, type it a valid number float.')
        except KeyboardInterrupt:
            n = 0 
            print(Fore.RED + f'The user not prefered type the floating number.')
        else:
            is_correct = True
    
    return n


integ = readInteger()    
floatg = readFloat()

print(f'The integer value typed was {integ} and the floating was {floatg}')