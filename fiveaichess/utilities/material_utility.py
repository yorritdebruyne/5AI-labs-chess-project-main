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
        chess.PAWN: 100, # Values increased to centipawns for precision
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900
    }

    # Piece-Square Tables: Bonus points per field from White's point of view
    # Pawns are encouraged to stay in the center and advance forward
    pst = {
        chess.PAWN: [
             0,  0,  0,  0,  0,  0,  0,  0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
             5,  5, 10, 27, 27, 10,  5,  5,
             0,  0,  0, 25, 25,  0,  0,  0,
             5, -5,-10,  0,  0,-10, -5,  5,
             5, 10, 10,-25,-25, 10, 10,  5,
             0,  0,  0,  0,  0,  0,  0,  0
        ],
        # Knights are encouraged to control the center and stay away from edges to increase mobility
         chess.KNIGHT : [
             -50, -40, -30, -30, -30, -30, -40, -50,
             -40, -20,   0,   0,   0,   0, -20, -40,
             -30,   0,  10,  15,  15,  10,   0, -30,
             -30,   5,  15,  20,  20,  15,   5, -30,
             -30,   0,  15,  20,  20,  15,   0, -30,
             -30,   5,  10,  15,  15,  10,   5, -30,
             -40, -20,   0,   5,   5,   0, -20, -40,
             -50, -40, -30, -30, -30, -30, -40, -50
         ],
        # Bishops are encouraged to control the center and stay away from edges and corners
        chess.BISHOP : [
            -20,-10,-10,-10,-10,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5, 10, 10,  5,  0,-10,
            -10,  5,  5, 10, 10,  5,  5,-10,
            -10,  0, 10, 10, 10, 10,  0,-10,
            -10, 10, 10, 10, 10, 10, 10,-10,
            -10,  5,  0,  0,  0,  0,  5,-10,
            -20,-10,-40,-10,-10,-40,-10,-20,
        ]
    }

    # Count all white & black pieces and their value.
    # Subtract them to see which one is in a better position
    def board_value(self, board : Board):
        score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                val = self.piece_values.get(piece.piece_type, 0)
                # Add PST bonus
                if piece.piece_type in self.pst:
                    # Mirroring for black since pst is initialized for white
                    pst_idx = square if piece.color == chess.WHITE else chess.square_mirror(square)
                    val += self.pst[piece.piece_type][pst_idx]
                if piece.color == chess.WHITE:
                    score += val
                else:
                    score -= val
        return score / 100.0 # Back to original scale
        # n_white = 0
        # n_black = 0
        # for piece, value in self.piece_values.items():
        #     n_white += len(board.pieces(piece, chess.WHITE)) * value
        #     n_black += len(board.pieces(piece, chess.BLACK)) * value
        # return n_white - n_black
