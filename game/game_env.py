import retro

def create_game_environment(game, state):
    env = retro.make(game, state)
    return env
