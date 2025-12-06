import time
import random
from platform import machine

import chess

from chess import Board, Move

from fiveaichess.agents.agent import Agent
from fiveaichess.utilities.utility import Utility

"""
Minimax Agent with alpha-beta pruning
-------------------------------------
This agent uses a search algorithm to evaluate moves.
He can use minimax with or without alpha-beta pruning.
Alpha-beta pruning realises the same output as the classic minimax,
but calculates faster by pruning the branches 
when they are not relevant anymore.

"""


class MinimaxAgent(Agent):
    name = "5AIChessAgent"

    author = "Sander&Yorrit"

    def __init__(self, utility : Utility, time_limit_move : float, depth):
        super().__init__(utility, time_limit_move)
        # Save in class
        self.depth = depth

    # ---------------------------------------
    # --- Classic minimax without pruning ---
    # ---------------------------------------

    # Recursively simulates future moves to evaluate board positions
    def minimax(self, board : Board , depth : int, maximizing_player : bool):

        # If depth = empty or the game is over: give evaluation back
        if depth == 0 or board.is_game_over():
            return self.utility.board_value(board)

        # Player is maximizing player
        if maximizing_player:
            best_value = - float('inf')
            for move in list(board.legal_moves):
                # Play move
                board.push(move)
                # Calculate new value
                value = self.minimax(board, depth - 1, False)
                # Reverse move
                board.pop()
                # Evaluate values until the optimal move is determined
                best_value = max(value, best_value)
            return best_value

        # Player is minimizing player
        else:
            worst_value = float('inf')
            for move in list(board.legal_moves):
                # Play move
                board.push(move)
                # Evaluate recursively
                value = self.minimax(board, depth - 1, True)
                # Reverse move
                board.pop()
                # Evaluate values until the optimal move is determined
                worst_value = min(value, worst_value)
            return worst_value

    #-----------------------------------
    # --- Alpha-beta pruning version ---
    # ----------------------------------

    def alphabeta(self, board : Board, depth : int, alpha : float, beta : float, maximizing_player : bool):
        # If depth = empty or the game is over: give evaluation back
        if depth == 0 or board.is_game_over():
            return self.utility.board_value(board)

        # Player is maximizing player
        if maximizing_player:
            best_value = - float('inf')
            for move in list(board.legal_moves):
                # Play move
                board.push(move)
                # Calculate new value
                value = self.alphabeta(board, depth - 1, alpha, beta, False)
                # Reverse move
                board.pop()
                # Evaluate values until the optimal move is determined
                best_value = max(value, best_value)
                # Evaluate if alpha is the highest value
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break # Prune: no value in searching any further
            return best_value

        # Player is minimizing player
        else:
            worst_value = float('inf')
            for move in list(board.legal_moves):
                # Play move
                board.push(move)
                # Evaluate recursively
                value = self.alphabeta(board, depth - 1, alpha, beta,True)
                # Reverse move
                board.pop()
                # Evaluate values until the optimal move is determined
                worst_value = min(value, worst_value)
                # Evaluate if beta is the lowest value
                beta = min(beta, worst_value)
                if beta <= alpha:
                    break  # Prune: no value in searching any further
            return worst_value

    # ----------------------
    # --- Move Selection ---
    # ----------------------

    # Chooses the best current move by evaluating all options with alpha-beta pruning
    def calculate_move(self, board: Board, constraints: dict[str, int] = {}) -> Move:
        start_time = time.time()

        best_move = None

        # WHITE = maximizing player: wants to maximize score
        # BLACK = minimzing player: wants to minimize the player's score
        maximizing_player = True if board.turn == chess.WHITE else False

        alpha = - float('inf')
        beta = float('inf')

        if maximizing_player:
            best_value = - float('inf')
            for move in list(board.legal_moves):

                # Check if the maximum calculation time for this move has been reached
                if time.time() - start_time > self.time_limit_move:
                    break # When time is exceeded

                # Play move
                board.push(move)

                # Calculate new value with minimax
#                value = self.minimax(board, self.depth - 1, False)

                # Calculate new value with alphabeta pruning
                value = self.alphabeta(board, self.depth - 1, alpha, beta, False)

                # Reverse move
                board.pop()

                # Update best_value and best_move if this move is better
                if value > best_value:
                    best_value = value
                    best_move = move


            return best_move

        else:
            worst_value = float('inf')
            for move in list(board.legal_moves):

                # Check if the maximum calculation time for this move has been reached
                if time.time() - start_time > self.time_limit_move:
                    break # When time is exceeded

                # Play move
                board.push(move)

                # Calculate new value with minimax
#                value = self.minimax(board, self.depth - 1, True)

                # Calculate new value with alphabeta pruning
                value = self.alphabeta(board, self.depth - 1, alpha, beta, True)

                # Reverse move
                board.pop()

                # Update worst_value and best_move if this move is better (lower)
                if value < worst_value:
                    worst_value = value
                    best_move = move

            return best_move
