seq = []
n = 0
c = 1

while c < 99:
    n = int(input(f'{c} - Digite um valor [0:Stop]: '))
    
    if n == 0 and c > 1:
        break
    elif n == 0 and c == 1:
        print("\n é necessario mais de 1 numero na lista. \n")
    
    for num in seq:
        if n == num:
            print(f'\n {n} Já é existente na lista, Adicione outro. \n')
            break

    if c == 1 and n != 0:
        c += 1
        seq.append(n)
    
    if c > 1 and n != 0:
        if not n in seq:
            c += 1
            seq.append(n)  

        
seq.sort()
print(seq)
    