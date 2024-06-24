print("Sequência de Fibonacci")
termos = int(input("Quantos termos você quer mostrar? : "))
print(" ")

ant = 0
actual = 1
initial = 0 
print(f'{ant} => {actual}', end='')

while initial <= termos:
    next = ant + actual
    print(f' => {next}', end='')
    ant = actual
    actual = next    
    
    initial += 1

print(" FIM", end='')