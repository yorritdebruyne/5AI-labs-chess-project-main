import chess

from chess import Board, Move

from fiveaichess.utilities.utility import Utility


"""
KingSafetyUtility
---------------
Evaluates a board position based on king safety.
- Looks at the squares directly in front of the king (rank +1 for White, rank -1 for Black).
- Checks the three files around the king (file-1, file, file+1).
- Counts how many of those squares are protected by pieces of the same color.
- If a square is outside the board (edge/muur), it counts as protection.
Positive score : WHITE king = safer
Negative score : BLACK king = safer
"""

class KingSafetyUtility(Utility):

    def board_value(self, board: Board):
        white_score = self._king_safety(board, chess.WHITE)
        black_score = self._king_safety(board, chess.BLACK)
        return white_score - black_score


    def _king_safety(self, board : Board, color : bool) -> int :

        # Get king square
        king_square = board.king(color)
        # Check if king exists
        if king_square is None:
            return 0 # Shouldn't happen normally

        # Get file (column) & rank (row) of the king
        king_file = chess.square_file(king_square)
        king_rank = chess.square_rank(king_square)

        # For WHITE: pawns are one rank ahead
        if color == chess.WHITE :
            direction = 1
        # For BLACK: pawns are one rank behind
        else:
            direction = -1

        # Calculate target_rank
        target_rank = king_rank + direction

        # Initialize safety point on 0
        safety_points = 0

        # Check the 3 files surrounding the king (file - 1, file, file + 1)
        for df in [-1, 0 , 1]:
            target_file = king_file + df

            # If the square is outside the board, count as protection ("wall")
            if not (0 <= target_file <= 7 and 0 <= target_rank <= 7):
                safety_points += 1
                continue

            square = chess.square(target_file, target_rank)
            piece = board.piece_at(square)

            # If there is a piece of the same color surrounding the king, count as protection.
            if piece and piece.color == color:
                safety_points += 1
            # TODO: Evaluate if the substraction is useful or an obstacle
            # else:
            #     safety_points -= 1
        return safety_points