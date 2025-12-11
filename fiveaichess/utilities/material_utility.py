import chess

from chess import Board, Move

from fiveaichess.utilities.utility import Utility


"""
material_utility
----------------
Evaluate a board position based on material balance.
Positive score = advantage for WHITE
Negative score = advantage for BLACK
"""

class MaterialUtility(Utility):

    # Values for pieces in a dictionary.
    # King gets no value, because he can't be sacrificed
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }

    # Count all white & black pieces and their value.
    # Subtract them to see which one is in a better position
    def board_value(self, board : Board):
        n_white = 0
        n_black = 0
        for piece, value in self.piece_values.items():
            n_white += len(board.pieces(piece, chess.WHITE)) * value
            n_black += len(board.pieces(piece, chess.BLACK)) * value
        return n_white - n_black
