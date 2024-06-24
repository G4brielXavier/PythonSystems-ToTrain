allplayers = []
player = {}

limit = int(input("How many players will be placers here? : "))
goals = []
tot = 0

for i in range(0, limit):
    print()
    player['Name'] = input("Player name: ")
    player['Matchs'] = int(input(f'How many matchs {player['Name']} was played? : '))
    for i in range(0, player['Matchs']):
        goals.append(int(input(f'How many goals in match {i}? : ')))

    player['Total'] = sum(goals)    
    player['Goals'] = goals[:]
    goals.clear()
    
    allplayers.append(player.copy())
    player.clear()
    
print()

for i, v in enumerate(allplayers):
    print(f'{i} {v['Name']} | {v['Goals']} | {v['Total']}')

print()

def search(core_main):
    indx = int(input("indx to search: "))
    play_seq = core_main[indx]
    print()
    print(f'About the {core_main[indx]['Name']}')
    print()
    for i, v in enumerate(play_seq['Goals']):
        print(f'in Match {i} he was did {v} goals.')
    
    
search(allplayers)