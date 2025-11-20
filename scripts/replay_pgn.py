import os

import chess.pgn

"""
Replay a chess game from a PGN file
"""
def replay_pgn(pgn_file_path):
    # open the pgn file with the game information
    with open(pgn_file_path) as pgn_file:
        # read the game file until the end
        while pgn_game := chess.pgn.read_game(pgn_file):
            board = pgn_game.board()
            # play the sequence of moves specified in the file
            for move in pgn_game.mainline_moves():
                print(board)
                print('------------------------------')
                board.push(move)


if __name__ == '__main__':
    example_pgn = os.path.join(os.path.dirname(__file__), '../data/kasparov-deep-blue-1997.pgn')
    replay_pgn(example_pgn)
