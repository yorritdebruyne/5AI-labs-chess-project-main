import chess
from chess import Board

from fiveaichess.utilities.utility import Utility

from fiveaichess.utilities.material_utility import MaterialUtility
from fiveaichess.utilities.mobility_utility import MobilityUtility
from fiveaichess.utilities.king_safety_utility import KingSafetyUtility
from fiveaichess.utilities.checking import check
from fiveaichess.utilities.pawnpush import pawnPush


"""
CombinedUtility
---------------
Evaluates a board position by combining multiple evaluation strategies:
- MaterialUtility: counts the material balance (pieces and their values)
- MobilityUtility: counts the number of legal moves for both sides
- ...
The final score is a weighted sum of all evaluations.
Positive score = advantage for WHITE
Negative score = advantage for BLACK
"""
n = 0
class CombinedUtility(Utility):

    def __init__(self):
        # Create instances of the individual utilities
        self.material = MaterialUtility()
        self.mobility = MobilityUtility()
        self.kingsafety = KingSafetyUtility()
        self.pawnPush = pawnPush()
        self.check = check()

    def board_value(self, board: Board):

        # Define weights: adjustable if a factor is more important

        if board.ply() < 10: #begingame
            material_weight = 2
            mobility_weight = 0.2
            kingsafety_weight = 1
            checkmate_weight = 0.5
            pawnpush_weight = 0
        elif board.ply() < 25: #middlegame
            material_weight = 1.3
            mobility_weight = 0.7
            kingsafety_weight = 1
            checkmate_weight = 1
            pawnpush_weight = 1
        else:
            material_weight = 1.0
            mobility_weight = 1.3
            kingsafety_weight = 0.2
            checkmate_weight = 3
            pawnpush_weight = 2

        # TODO: add other weights
        pawnpush_weight = 0 # TODO: sometimes it returns strange values ==> need to inspect the function.
        # Get the evaluation from MaterialUtility (piece values)
        material_score = self.material.board_value(board)
        # Get the evaluation from MobilityUtility (number of legal moves)

        mobility_score = self.mobility.board_value(board)
        # Get the evaluation from KingSafetyUtility (score based on filled/empty squares surrounding king)
        kingsafety_score = self.kingsafety.board_value(board)
        # TODO: add more utilities
        check_score = self.check.board_value(board)
        """
        global n
        n += 1
        """

        pawnpush_score = self.pawnPush.board_value(board)


        # Combine the scores using the chosen weights
        combined_score = material_score * material_weight + mobility_score * mobility_weight + \
                         kingsafety_score * kingsafety_weight + check_score * checkmate_weight + \
                         pawnpush_score * pawnpush_weight  # TODO: add the rest
        """
        if board.is_checkmate():
            print("jawel checkmaat")
            moves = [m.uci() for m in board.move_stack]
            print("mat: , mob: , king: , check: , pawn: , comb: ",material_score,mobility_score,kingsafety_score,check_score,pawnpush_score,combined_score)
            print(moves)
            print("n: ", n)

        
        global n
        n += 1
        moves = [m.uci() for m in board.move_stack]
        with open("eval_log(1).txt", "a") as f:
            f.write(
                f"{material_score},"
                f"{mobility_score},"
                f"{kingsafety_score},"
                f"{check_score},"
                f"{pawnpush_score},"
                f"{combined_score}\n"
            )
            print(moves, file=f)
            print("n: ", n)
            print("\n")
        """
        """
        if combined_score > 10 or combined_score < -10:
            print("mat: , mob: , king: , check: , pawn: , comb: ",material_score,mobility_score,kingsafety_score,check_score,pawnpush_score,combined_score)
            moves = [m.uci() for m in board.move_stack]
            print(moves)
            print(n)
            print("\n")"""
        # Return the final combined evaluation
        return combined_score*0.1
