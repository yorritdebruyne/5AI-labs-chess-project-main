from abc import ABC, abstractmethod

from chess import Board


"""
An abstract base class for chess game state utility functions
"""
class Utility(ABC):
    
    @abstractmethod
    def board_value(self, board: Board): ...
        # determine the value of the current board: high is good for white, low is good for black, 0 is neutral
