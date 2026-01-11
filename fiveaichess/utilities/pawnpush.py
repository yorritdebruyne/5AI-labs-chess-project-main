import chess

from chess import Board, Move

from fiveaichess.utilities.utility import Utility


"""  In de endgame is het belangrijk dat de pawns gepusht worden.
     Passed pawn krijgt meer punten dan een gewone pawn aangezien die meer kans hebben om gepromoveerd te worden.
     Doubled pawns krijgen minder punten aangezien deze elkaar in de weg zitten.
     Connected pawns krijgen ook meer punten aangezien deze elkaar beschermen.
"""

class pawnPush(Utility):

    def board_value(self, board: Board):
        return self.pawnPush(board)

    def pawnPush(self, board: Board) -> int:
        # doubled pawns checken
        doubledWhite = 0
        doubledBlack = 0
        pushedWhite = 0
        pushedBlack = 0
        whitePawns = board.pieces(chess.PAWN, chess.WHITE)
        whitePawnsList = []
        blackPawns = board.pieces(chess.PAWN, chess.BLACK)
        blackPawnsList = []
        if board.turn == chess.WHITE:
            # Doubled pawns: If it is white turn doubled pawns for white are bad and for black are good
            # Pushed Pawns: If white pawns are further on the board thats better for white and worse for black
            for Wpawn in whitePawns:
                pawn_file = Wpawn%8
                if pawn_file in whitePawnsList:
                    doubledWhite -= 1
                whitePawnsList.append(pawn_file)
                pawn_rank = Wpawn // 8
                for i in range(3,8):
                    if pawn_rank < i:
                        pushedWhite += i - 1

            for Bpawn in blackPawns:
                pawn_file = Bpawn%8
                if pawn_file in blackPawnsList:
                    doubledBlack += 1
                blackPawnsList.append(pawn_file)
                pawn_rank = Bpawn // 8
                for i in range(3, 8):
                    if pawn_rank < i:
                        pushedBlack -= i - 1

        else:
            for Wpawn in whitePawns:
                pawn_file = Wpawn% 8
                if pawn_file in whitePawnsList:
                    doubledWhite += 1
                whitePawnsList.append(pawn_file)
                pawn_rank = Wpawn // 8
                for i in range(3, 8):
                    if pawn_rank < i:
                        pushedWhite -= i - 1
            for Bpawn in blackPawns:
                pawn_file = Bpawn % 8
                if pawn_file in blackPawnsList:
                    doubledBlack -= 1
                blackPawnsList.append(pawn_file)
                pawn_rank = Bpawn // 8
                for i in range(3, 8):
                    if pawn_rank < i:
                        pushedBlack += i - 1
        return 0
        #TODO Check this function, returns values like -220 and thats way to high
        #return doubledWhite - doubledBlack + pushedWhite - pushedBlack




