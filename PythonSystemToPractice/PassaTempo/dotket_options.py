def new_number_1():
    n = int(input(":] - Numero 1: "))
    return n 

def new_number_2():
    n = int(input(":] - Numero 2: "))
    return n

def options():
    print("______________________________________________")
    options_name = ["Somar", "Multiplicar", "Maior", "Alterar Números", "Sair do Programa"]
    for i, it in enumerate(options_name):
        print(f'[ {i} ] {it}')
        
    your_option = int(input(":] - Qual é sua opção? : "))
    return your_option

def conditions(option, n1, n2):    
    if option == 0:
        print(f':] - {n1} + {n2} = {n1 + n2}')
    elif option == 1:
        print(f':] - {n1} x {n2} = {n1 * n2}')
    elif option == 2:
        print(f':] - O Maior numero é {max(n1, n2)}')
    elif option == 3:
        print(":] - Defina os novos numeros.")
        n1 = new_number_1()
        n2 = new_number_2(  )
    elif option == 4:
        print(":] - Tchau!")
    
    if not option == 4:
        op = options()
        conditions(op, n1, n2)
        
    
v1 = new_number_1()
v2 = new_number_2()
op_1 = options()
conditions(op_1, v1, v2)
    
