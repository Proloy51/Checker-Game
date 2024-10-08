import pygame
import numpy as np
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from .board import Board
from collections import defaultdict

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.player_moves = 0
        self.ai_moves = 0
        self.moves_without_capture = 0  
        self.move_history = []  

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.player_moves = 0
        self.ai_moves = 0
        self.moves_without_capture = 0  
        self.move_history = []

    def winner(self):
        if self.board.red_left <= 0:
            return WHITE
        elif self.board.white_left <= 0:
            return RED

        if not self.board.has_legal_moves(RED):
            return WHITE
        if not self.board.has_legal_moves(WHITE):
            return RED
        
        position_counts = defaultdict(int)
        for pos in self.move_history:
            position_counts[pos] += 1
            if position_counts[pos] >= 3:
                return "Draw due to threefold repetition"

        if self.moves_without_capture >= 30:
            return "Draw due to 30-move rule"
        
        return None

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
                self.moves_without_capture = 0  
            else:
                self.moves_without_capture += 1  

            if self.turn == RED:
                self.player_moves += 1
            else:
                self.ai_moves += 1
          
            self.move_history.append(self.board_to_string())

            self.print_board_as_array()
            
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        self.turn = WHITE if self.turn == RED else RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.ai_moves += 1  
        self.move_history.append(self.board_to_string())  
        
        if self.board.move_count_without_capture >= 30:
            self.board.move_count_without_capture = 0 
        else:
            self.board.move_count_without_capture += 1 

        self.change_turn()

    def board_to_string(self):
        board_string = ''
        for row in self.board.board:
            for piece in row:
                if piece == 0:
                    board_string += '0'
                elif piece.color == RED:
                    board_string += 'r' if not piece.king else 'R'
                elif piece.color == WHITE:
                    board_string += 'w' if not piece.king else 'W'
        return board_string

    def print_board_as_array(self):
        board_array = np.zeros((8, 8), dtype=int)
        for i, row in enumerate(self.board.board):
            for j, piece in enumerate(row):
                if piece == 0:
                    board_array[i, j] = 0
                elif piece.color == RED:
                    board_array[i, j] = -1 if not piece.king else -2
                elif piece.color == WHITE:
                    board_array[i, j] = 1 if not piece.king else 2
        print(board_array)
        
        
    def get_all_pieces(self, color):
        return [piece for piece in self.board.pieces if piece.color == color]
        
        
    def get_possible_moves(self):
        possible_moves = []
        for piece in self.board.get_all_pieces(self.turn):
            moves = self.get_legal_moves_for_piece(piece)
            possible_moves.extend(moves)

        return possible_moves
    
    
    def get_legal_moves_for_piece(self, piece):
        moves = []
        row, col = piece.row, piece.col
        direction = 1 if piece.color == WHITE else -1 

        for dr, dc in [(direction, -1), (direction, 1)]:
            new_row, new_col = row + dr, col + dc
            if self.is_within_bounds(new_row, new_col):
                if not self.get_piece(new_row, new_col):
                    moves.append((row, col, new_row, new_col))
                elif self.get_piece(new_row, new_col).color != piece.color:
                    capture_row, capture_col = row + 2 * dr, col + 2 * dc
                    if self.is_within_bounds(capture_row, capture_col) and not self.get_piece(capture_row, capture_col):
                        moves.append((row, col, capture_row, capture_col))  

        # King piece moves (if piece is a king)
        if piece.king:
            for dr, dc in [(-direction, -1), (-direction, 1)]: 
                new_row, new_col = row + dr, col + dc
                while self.is_within_bounds(new_row, new_col):
                    if not self.get_piece(new_row, new_col):
                        moves.append((row, col, new_row, new_col)) 
                    elif self.get_piece(new_row, new_col).color != piece.color:
                        capture_row, capture_col = new_row + dr, new_col + dc
                        if self.is_within_bounds(capture_row, capture_col) and not self.get_piece(capture_row, capture_col):
                            moves.append((row, col, capture_row, capture_col)) 
                        break 
                    else:
                        break

                    new_row += dr
                    new_col += dc

        return moves

def is_within_bounds(self, row, col):
    return 0 <= row < self.rows and 0 <= col < self.cols

def get_piece(self, row, col):
    return self.board[row][col] if self.is_within_bounds(row, col) else None

