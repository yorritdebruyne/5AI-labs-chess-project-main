from abc import ABC, abstractmethod

from chess import Board, Move

from fiveaichess.utilities.utility import Utility


"""
An abstract base class for chess agents
"""
class Agent(ABC):

    name: str

    author: str

    def __init__(self, utility: Utility, time_limit_move: float):
        self.utility = utility
        self.time_limit_move = time_limit_move

    @abstractmethod
    def calculate_move(self, board: Board, constraints: dict[str, int] = {}) -> Move: ...
        # calculate the next move based on the board's utility value