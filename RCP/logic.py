from random import choice

GAME_DOMINATION_RULES = {
    'p': 'r',
    'r': 'c',
    'c': 'p'
}
GAME_RULES_TRANSLATE = {
    'p': 'Paper',
    'r': 'Rock',
    'c': 'Cisors'
}


def player_dominates(player_choice, cpu_choice):
    rules = list(GAME_DOMINATION_RULES.keys())
    if player_choice in rules and cpu_choice in rules:
        return GAME_DOMINATION_RULES[player_choice] == cpu_choice
    return None


def generate_cpu_next_move():
    return choice(list(GAME_DOMINATION_RULES.keys()))
