import chess

from fiveaichess.agents.example_agent import ExampleAgent
from fiveaichess.utilities.example_utility import ExampleUtility
from fiveaichess.agents.minimax_agent import MinimaxAgent
from fiveaichess.utilities.material_utility import MaterialUtility


"""
Let two agents play a game against each other
"""
def play_self():
    board = chess.Board()

    # create the white and black players
#    white_player = ExampleAgent(ExampleUtility(), 5.0)
    white_player = MinimaxAgent(MaterialUtility(), 5.0, depth=3)
    white_player.name = "White Player"
    black_player = ExampleAgent(ExampleUtility(), 5.0)
#    black_player = MinimaxAgent(ExampleUtility(), 5.0, depth=2)
    black_player.name = "Black Player"

    running = True
    turn_white_player = True

    # game loop
    while running:
        move = None

        if turn_white_player:
            move = white_player.calculate_move(board)
            turn_white_player = False
            print(f'{white_player.name} plays {move}')
        else:
            move = black_player.calculate_move(board)
            turn_white_player = True
            print(f'{black_player.name} plays {move}')

        board.push(move)
        print(board)
        print('------------------------------')
        
        # check if a player has won
        if board.is_checkmate():
            running = False
            if turn_white_player:
                print(f"{black_player.name} wins!")
            else:
                print(f"{white_player.name} wins!")

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
        

if __name__ == '__main__':
    play_self()
