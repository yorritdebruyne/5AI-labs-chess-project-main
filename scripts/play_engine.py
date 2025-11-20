import os

import chess
import chess.engine

from fiveaichess.agents.example_agent import ExampleAgent
from fiveaichess.utilities.example_utility import ExampleUtility


"""
Let your agent play a game against Stockfish or another UCI engine
"""
def play_other_engine(uci_engine_path: str, time_limit: float = 5.0):
    board = chess.Board()
    limit = chess.engine.Limit(time=time_limit)

    # define your agent here
    white_player = ExampleAgent(ExampleUtility(), 5.0)

    # connect to the uci engine
    black_player = chess.engine.SimpleEngine.popen_uci(uci_engine_path)
    # set stockfish's skill level
    black_player.configure({'Skill Level': 1})

    running = True
    turn_white_player = True

    # game loop
    while running:
        move = None

        if turn_white_player:
            move = white_player.calculate_move(board)
            turn_white_player = False
            print(f"{white_player.name} plays {move}")
        else:
            move = black_player.play(board, limit).move
            turn_white_player = True
            print(f"{black_player.id['name']} plays {move}")

        board.push(move)
        print(board)
        print('------------------------------')
        
        # check if a player has won
        if board.is_checkmate():
            running = False
            if turn_white_player:
                print('Stockfish wins!')
            else:
                print(f'{white_player.name} wins!')

        # check for draws
        if board.is_stalemate():
            running = False
            print('Draw by stalemate')
        elif board.is_insufficient_material():
            running = False
            print('Draw by insufficient material')
        elif board.is_fivefold_repetition():
            running = False
            print('Draw by fivefold repitition!')
        elif board.is_seventyfive_moves():
            running = False
            print('Draw by 75-moves rule')

    black_player.quit()


if __name__ == '__main__':

    uci_engine_path = os.getenv('UCI_ENGINE_PATH')

    if not uci_engine_path:
        raise EnvironmentError('Environment variable UCI_ENGINE_PATH not defined')
    
    play_other_engine(uci_engine_path)
