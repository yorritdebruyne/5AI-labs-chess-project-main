import chess

from chess import Board, Move

from fiveaichess.utilities.utility import Utility


"""
MobilityUtility
---------------
Evaluates a board position based on mobility.
- Counts the number of legal moves for both WHITE & BLACK
- Returns the difference between WHITE moves and BLACK moves
Positive score = advantage for WHITE (more options)
Negative score = advantage for BLACK (more options)
"""

class MobilityUtility(Utility):


    def board_value(self, board: Board):

        # Save the original turn so we can restore it later
        original_board_turn = board.turn

        # Temporary set turn to WHITE
        board.turn = chess.WHITE
        # Count legal moves for WHITE
        mobility_white = len(list(board.legal_moves))

        # Temporary set turn to BLACK
        board.turn = chess.BLACK
        # Count legal moves for BLACK
        mobility_black = len(list(board.legal_moves))

        # Restore the original turn to avoid disturbing the game flow
        board.turn = original_board_turn

        # Return the difference: positive means White has more mobility
        return (mobility_white - mobility_black) * 0.5

