from random import randint

vitorias = 0

def ver(vit):
    if vit >= 0 and vit < 2:
        print(f':] - Foi {vit} vitorias, você tentou.')
    elif vit >= 2 and vit < 4:
        print(f':] - Foram {vit} vitorias, Sorte? ou não?')
    elif vit >= 4 and vit < 6:
        print(f':] - Ok, {vit} vitorias, você é bom, admito(Sortudo)')
    elif vit > 6 and vit < 10:
        print(f':] - A Sorte Encarnada, {vit} vitorias')
    elif vit > 10:
        print(f':] - STOP NOW! ({vit}] vitorias.')

def validation():
    global vitorias
    
    option = input(":] - Par ou ímpar?: ").lower()
    print(" ")
    
    if option == "par":
        print(f':] - Ok, você escolheu PAR então eu sou ÍMPAR.')
    else:
        print(f':] - Ok, você escolheu ÍMPAR então eu sou PAR.')
        
    n_computer = randint(0, 10)
    your_number = int(input(":] - Escolha um numero de 1 a 10: "))
    
    print(" ")
    print(f':] - Eu escolhi {n_computer} e você {your_number}')

    total = n_computer + your_number
    
    if total % 2 == 0:
        if option == "par":
            print(f':[ - {total} é PAR, perdi.')
            vitorias += 1
            validation()
        else:
            print(f':] - {total} é PAR, ganhei.')
            print(" ")
            ver(vitorias)
            vitorias = 0
    else:
        if option == "impar":
            print(f':[ - {total} é ÍMPAR, perdi')
            vitorias += 1
            validation()
        else:
            print(f':] - {total} é ÍMPAR, ganhei.')
            ver(vitorias)
            vitorias = 0
     
print(":] - Vamos Brincar de PAR ou ÍMPAR.")
print(" ")       
validation()