import chess

from chess import Board, Move

from fiveaichess.utilities.utility import Utility


"""  Check utility zodat het doel niet is om zoveel mogelijk stukken van de andere te pakken maar om de andere koning
     geen beweginsmogelijkheden meer te geven.
"""

class check(Utility):

    def board_value(self, board: Board):
        if board.turn == chess.WHITE:
            color = True
        else:
            color = False
        score = self.checkmatePossibility(board, color)
        return score

    def checkmatePossibility(self, board: Board, color : bool) -> int:
        if color:
            if board.is_check():
                return -5
            elif board.is_checkmate():
                return -1000
        else:
            if board.is_check():
                return 5
            elif board.is_checkmate():
                return 1000
        return 0





