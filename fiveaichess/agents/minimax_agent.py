import time
import random

import chess

from chess import Board, Move

from fiveaichess.agents.agent import Agent
from fiveaichess.utilities.utility import Utility

"""
An example of a chess agent that provides a naive implementation

This agent iterates trough all the moves possible and picks the one with the highest utility.

"""


class MinimaxAgent(Agent):
    name = "5AIChessAgent"

    author = "SanderEN&Yorrit"

    def __init__(self, utility: Utility, time_limit_move: float):
        super().__init__(utility, time_limit_move)
        # initialize your agent with additional parameters if needed

    def calculate_move(self, board: Board, constraints: dict[str, int] = {}) -> Move:
        start_time = time.time()

        # if the agent is playing as black, the utility values are flipped (negative-positive)
        flip_value = 1 if board.turn == chess.WHITE else -1

        best_move = random.sample(list(board.legal_moves), 1)[0]
        best_utility = 0

        # loop trough all legal moves
        for move in list(board.legal_moves):

            # check if the maximum calculation time for this move has been reached
            if time.time() - start_time > self.time_limit_move:
                break

            # play the move
            board.push(move)

            # determine the value of the board after this move
            value = flip_value * self.utility.board_value(board)

            # if this is better than all other previous moves, store this move and its utility
            if value > best_utility:
                best_move = move
                best_utility = value

            # revert the board to its original state
            board.pop()

        return best_move
