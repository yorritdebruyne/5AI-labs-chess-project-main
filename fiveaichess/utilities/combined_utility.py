import chess
from chess import Board

from fiveaichess.utilities.utility import Utility

from fiveaichess.utilities.material_utility import MaterialUtility
from fiveaichess.utilities.mobility_utility import MobilityUtility
from fiveaichess.utilities.king_safety_utility import KingSafetyUtility


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


class CombinedUtility(Utility):

    def __init__(self):
        # Create instances of the individual utilities
        self.material = MaterialUtility()
        self.mobility = MobilityUtility()
        self.kingsafety = KingSafetyUtility()

    def board_value(self, board: Board):

        # Define weights: adjustable if a factor is more important
        material_weight = 1.0
        mobility_weight = 1
        kingsafety_weight = 1
        # TODO: add other weights

        # Get the evaluation from MaterialUtility (piece values)
        material_score = self.material.board_value(board)
        # Get the evaluation from MobilityUtility (number of legal moves)
        mobility_score = self.mobility.board_value(board)
        # Get the evaluation from KingSafetyUtility (score based on filled/empty squares surrounding king)
        kingsafety_score = self.kingsafety.board_value(board)
        # TODO: add more utilities

        # Combine the scores using the chosen weights
        combined_score = material_score * material_weight + mobility_score * mobility_weight + kingsafety_score * kingsafety_weight# TODO: add the rest
        # Return the final combined evaluation
        return combined_score