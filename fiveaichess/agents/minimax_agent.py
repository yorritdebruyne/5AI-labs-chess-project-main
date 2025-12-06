import time
import random
from platform import machine

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

    author = "Sander&Yorrit"

    def __init__(self, utility : Utility, time_limit_move : float, depth):
        super().__init__(utility, time_limit_move)
        self.depth = depth # Save in class


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

    # Chooses the best current move by evaluating all options with minimax
    def calculate_move(self, board: Board, constraints: dict[str, int] = {}) -> Move:
        startTime = time.time()

        best_move = None

        # WHITE = maximizing player: wants to maximize score
        # BLACK = minimzing player: wants to minimize the player's score
        maximizing_player = True if board.turn == chess.WHITE else False

        if maximizing_player:
            best_value = - float('inf')
            for move in list(board.legal_moves):
                # Play move
                board.push(move)
                # Calculate new value
                value = self.minimax(board, self.depth - 1, False)
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
                # Play move
                board.push(move)
                # Calculate new value
                value = self.minimax(board, self.depth - 1, True)
                # Reverse move
                board.pop()

                # Update worst_value and best_move if this move is better (lower)
                if value < worst_value:
                    worst_value = value
                    best_move = move

            return best_move
