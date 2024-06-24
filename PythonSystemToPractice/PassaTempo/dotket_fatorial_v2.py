print("Dotket Company :]")
print("Gerador de PA v2.0 - :]")
print(" ")

termo_initial = int(input(":] - Qual o primeiro Termo? : "))
razao = int(input(":] - Qual a razão da PA? : "))

attemps = 0
initial_base = 0
termos_created = 0
final_base = 10 # valor base de final de termo

base = termo_initial

def PA(razao, base, initial, final, total):
    global attemps
    f = 0

    if not attemps == 0:
        f = initial + final
    else:
        f = final    

    attemps += 1
    
    while initial < f:
        print(f'{base} => ', end='')
        total += 1
        initial += 1
        base += razao

    
    print("PAUSA \n", end='')
    more_terms = int(input(":] - Quantos termos você deseja ver mais? [ 0:Fechar ]: "))
    
    if more_terms == 0:
        print(f':] - Você criou {total} termos')
    else:
        PA(razao, base, initial, more_terms, total)
 
PA(razao, base, termo_initial, final_base, termos_created)      
