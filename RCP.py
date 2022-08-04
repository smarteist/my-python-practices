from datetime import datetime

from RCP.logic import generate_cpu_next_move, GAME_RULES_TRANSLATE, player_dominates

print(
    'Hello! This is ROCK CISORS AND PAPER!',
    'Select your Move Between [ r, c, p]'
    'You Can enter [reset] to reset the game!'
    'You Can enter [exit] to finish the game!',
    sep='\n'
)

result = [0, 0]
start_time = datetime.now()

while True:
    player_move = input("Enter your move [r | c | p]?\n")
    cpu_move = generate_cpu_next_move()
    if player_move == 'exit':
        timediff = datetime.utcfromtimestamp(
            (datetime.now() - start_time).total_seconds()
        )
        print(f'GoodBye! We played {timediff.strftime("%M")} minutes and {timediff.strftime("%S")} soconds')
        exit()
    elif player_move == 'clear':
        result = [0, 0]
    elif cpu_move == player_move:
        print('Draw! im {} too!'.format(GAME_RULES_TRANSLATE[cpu_move]))
    else:
        playerdominates = player_dominates(player_move, cpu_move)
        if playerdominates is None:
            print('What? Plaese enter a valid input!')
        elif playerdominates:
            result[0] += 1
            print('You Win! im {} and you {}!'.format(
                GAME_RULES_TRANSLATE[cpu_move],
                GAME_RULES_TRANSLATE[player_move]
            ), sep='\n')
        else:
            result[1] += 1
            print('You Lost! im {} and you {}!'.format(
                GAME_RULES_TRANSLATE[cpu_move],
                GAME_RULES_TRANSLATE[player_move]
            ), sep='\n')
        print('Result: You={}, Me={}'.format(result[0], result[1]), sep='\n')
