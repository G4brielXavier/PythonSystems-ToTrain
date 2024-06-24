from Modules import *

def validate_money(value):
    n = input(Fore.WHITE + value).replace(',', '.')
    
    n.strip()
    
    if n == '':
        print(Fore.RED + f'InvalidError - unknown value')
        n = validate_money(value)

    if n.isdigit() is False:
        print(Fore.RED + f'TypeError - this value {n} not is numeric type')
        n = validate_money(value)
        
    if not n == '' and n.isdigit() is True:
        return n
        
    
        