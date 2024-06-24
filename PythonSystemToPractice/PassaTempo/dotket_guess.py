from random import randint
from time import sleep

# guess game v2.0 in python
print("Conectando-se ao Dotket /")
sleep(2)
print(":] - Oi, Eu sou Dotket Computer.")
sleep(1)
print(":] - Eu acabei de escolher um numero entre 0 e 10.")
sleep(1)
print(":] - Tente adivinhar qual é.")
sleep(1)
print(" ")
def is_computer_think():
    n = randint(0, 11)
    return n

def is_client_guess(n, c):
    yn = int(input("You - is "))
    count = c
    
    if not yn == n:
        if yn < n:
            print(":/ - É mais, tente mais uma vez.")
            count += 1
            is_client_guess(n, count)
        elif yn > n:
            print(":/ - É menos, tente mais uma vez.")
            count += 1
            is_client_guess(n, count)
    else:
        print(f':] - Incrivel, Parabens, Em {count} tentativas, O numero que eu escolhí, O "{yn}", foi acertado.')  
        
think_computer_number = is_computer_think()
count_bs = 0
is_client_guess(think_computer_number, count_bs)
