matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(0, 3):
    for y in range(0, 3):
        matrix[x][y] = int(input(f'Em [{x}, {y}]: '))
        
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matrix[x][y]:^5}]', end='')
    print()
    

tot_pares = 0
for x in range(0, 3):
    for y in range(0, 3):
        if matrix[x][y] % 2 == 0:
            tot_pares += matrix[x][y]
        
print(f'A Soma de todos os pares: {tot_pares}.')

third_column_tot = 0 
for i in matrix:
    third_column_tot += i[2]
    
print(f'A Soma dos valores da Terceira Coluna é {third_column_tot}')

print(f'O Maior valor da Segunda Linha é {max(matrix[1])}')