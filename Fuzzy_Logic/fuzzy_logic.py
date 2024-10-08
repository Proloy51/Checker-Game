import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import random


'''piece_advantage = ctrl.Antecedent(np.arange(-12, 13, 1), 'piece_advantage')
piece_advantage['low'] = fuzz.trimf(piece_advantage.universe, [-12, -12, 0])
piece_advantage['medium'] = fuzz.trimf(piece_advantage.universe, [-12, 0, 12])
piece_advantage['high'] = fuzz.trimf(piece_advantage.universe, [0, 12, 12])

positional_strength = ctrl.Antecedent(np.arange(0, 101, 1), 'positional_strength')
positional_strength['weak'] = fuzz.trimf(positional_strength.universe, [0, 0, 50])
positional_strength['average'] = fuzz.trimf(positional_strength.universe, [0, 50, 100])
positional_strength['strong'] = fuzz.trimf(positional_strength.universe, [50, 100, 100])


evaluation = ctrl.Consequent(np.arange(0, 101, 1), 'evaluation')
evaluation['poor'] = fuzz.trimf(evaluation.universe, [0, 0, 50])
evaluation['fair'] = fuzz.trimf(evaluation.universe, [0, 50, 100])
evaluation['good'] = fuzz.trimf(evaluation.universe, [50, 100, 100])'''


piece_advantage = ctrl.Antecedent(np.arange(-12, 13, 1), 'piece_advantage')
positional_strength = ctrl.Antecedent(np.arange(0, 101, 1), 'positional_strength')
evaluation = ctrl.Consequent(np.arange(0, 101, 1), 'evaluation')

piece_advantage['low'] = fuzz.trimf(piece_advantage.universe, [-12, -12, 0])
piece_advantage['medium'] = fuzz.trimf(piece_advantage.universe, [-12, 0, 12])
piece_advantage['high'] = fuzz.trimf(piece_advantage.universe, [0, 12, 12])

positional_strength['poor'] = fuzz.trimf(positional_strength.universe, [0, 0, 50])
positional_strength['average'] = fuzz.trimf(positional_strength.universe, [0, 50, 100])
positional_strength['strong'] = fuzz.trimf(positional_strength.universe, [50, 100, 100])

evaluation['bad'] = fuzz.trimf(evaluation.universe, [0, 0, 50])
evaluation['good'] = fuzz.trimf(evaluation.universe, [0, 50, 100])
evaluation['excellent'] = fuzz.trimf(evaluation.universe, [50, 100, 100])


'''rule1 = ctrl.Rule(piece_advantage['high'] & positional_strength['strong'], evaluation['good'])
rule2 = ctrl.Rule(piece_advantage['low'] & positional_strength['weak'], evaluation['poor'])
rule3 = ctrl.Rule(piece_advantage['medium'] & positional_strength['average'], evaluation['fair'])

# Create fuzzy control system
evaluation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
evaluation_sim = ctrl.ControlSystemSimulation(evaluation_ctrl)

# Define fuzzy evaluation function
def fuzzy_evaluate(board):
    # Example values for piece advantage and positional strength
    piece_advantage_value = calculate_piece_advantage(board)
    positional_strength_value = calculate_positional_strength(board)
    
    # Input to the fuzzy system
    evaluation_sim.input['piece_advantage'] = piece_advantage_value
    evaluation_sim.input['positional_strength'] = positional_strength_value
    
    # Compute the fuzzy evaluation
    evaluation_sim.compute()
    return evaluation_sim.output['evaluation']

# Placeholder functions for piece advantage and positional strength
def calculate_piece_advantage(board):
    # Implement the logic to calculate piece advantage
    return 0  # Example return value

def calculate_positional_strength(board):
    # Implement the logic to calculate positional strength
    return 50  # Example return value

'''

rule1 = ctrl.Rule(piece_advantage['low'] & positional_strength['poor'], evaluation['bad'])
rule2 = ctrl.Rule(piece_advantage['low'] & positional_strength['average'], evaluation['bad'])
rule3 = ctrl.Rule(piece_advantage['low'] & positional_strength['strong'], evaluation['good'])
rule4 = ctrl.Rule(piece_advantage['medium'] & positional_strength['poor'], evaluation['bad'])
rule5 = ctrl.Rule(piece_advantage['medium'] & positional_strength['average'], evaluation['good'])
rule6 = ctrl.Rule(piece_advantage['medium'] & positional_strength['strong'], evaluation['excellent'])
rule7 = ctrl.Rule(piece_advantage['high'] & positional_strength['poor'], evaluation['good'])
rule8 = ctrl.Rule(piece_advantage['high'] & positional_strength['average'], evaluation['excellent'])
rule9 = ctrl.Rule(piece_advantage['high'] & positional_strength['strong'], evaluation['excellent'])


evaluation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
evaluation_sim = ctrl.ControlSystemSimulation(evaluation_ctrl)

'''
# Define fuzzy evaluation function
def fuzzy_evaluate(board):
    # Example values for piece advantage and positional strength
    piece_advantage_value = calculate_piece_advantage(board)
    positional_strength_value = calculate_positional_strength(board)
    
    # Input to the fuzzy system
    evaluation_sim.input['piece_advantage'] = piece_advantage_value
    evaluation_sim.input['positional_strength'] = positional_strength_value
    
    # Compute the fuzzy evaluation
    evaluation_sim.compute()
    return evaluation_sim.output['evaluation']

# Placeholder functions for piece advantage and positional strength
def calculate_piece_advantage(board):
    # Implement the logic to calculate piece advantage
    red_pieces = len(board.get_all_pieces(RED))
    white_pieces = len(board.get_all_pieces(WHITE))
    return red_pieces - white_pieces

def calculate_positional_strength(board):
    # Implement the logic to calculate positional strength
    # Example criteria: number of pieces in the center, king pieces, etc.
    center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
    positional_strength = 0
    
    for piece in board.get_all_pieces(RED) + board.get_all_pieces(WHITE):
        if (piece.row, piece.col) in center_squares:
            positional_strength += 10
        if piece.king:
            positional_strength += 20
    
    return min(positional_strength, 100)'''
    
    
    
def fuzzy_evaluate(board):
    piece_advantage_value = calculate_piece_advantage(board)
    positional_strength_value = calculate_positional_strength(board)

    evaluation_sim.input['piece_advantage'] = piece_advantage_value
    evaluation_sim.input['positional_strength'] = positional_strength_value
  
    evaluation_sim.compute()
    return evaluation_sim.output['evaluation']

def calculate_piece_advantage(board):
    red_pieces = len(board.get_all_pieces(RED))
    white_pieces = len(board.get_all_pieces(WHITE))
    return red_pieces - white_pieces

def calculate_positional_strength(board):
    center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
    positional_strength = 0
    
    for piece in board.get_all_pieces(RED) + board.get_all_pieces(WHITE):
        if (piece.row, piece.col) in center_squares:
            positional_strength += 10
        if piece.king:
            positional_strength += 20
    
    return min(positional_strength, 100)










'''


import numpy as np

def generate_possible_moves(board_state, ai_piece=1, opponent_piece=-1):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Possible move directions
    capture_directions = [(2 * d[0], 2 * d[1]) for d in directions]  # Capture move directions

    def is_within_bounds(x, y):
        return 0 <= x < board_state.shape[0] and 0 <= y < board_state.shape[1]

    possible_moves = []

    for i in range(board_state.shape[0]):
        for j in range(board_state.shape[1]):
            if board_state[i, j] == ai_piece:
                # Check for normal moves
                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if is_within_bounds(new_i, new_j) and board_state[new_i, new_j] == 0:
                        new_board = board_state.copy()
                        new_board[i, j] = 0
                        new_board[new_i, new_j] = ai_piece
                        move = ((i, j), (new_i, new_j), new_board)
                        possible_moves.append(move)
                
                # Check for capture moves
                for capture_direction in capture_directions:
                    mid_i, mid_j = i + capture_direction[0] // 2, j + capture_direction[1] // 2
                    new_i, new_j = i + capture_direction[0], j + capture_direction[1]
                    if (
                        is_within_bounds(mid_i, mid_j) and is_within_bounds(new_i, new_j) and
                        board_state[mid_i, mid_j] == opponent_piece and board_state[new_i, new_j] == 0
                    ):
                        new_board = board_state.copy()
                        new_board[i, j] = 0
                        new_board[mid_i, mid_j] = 0
                        new_board[new_i, new_j] = ai_piece
                        move = ((i, j), (new_i, new_j), new_board)
                        possible_moves.append(move)

    return possible_moves








def generate_and_evaluate_moves(board_state):
    possible_moves = generate_possible_moves(board_state)
    evaluated_moves = []

    for move in possible_moves:
        fitness = fuzzy_evaluate(move[2])  # Use fuzzy logic for evaluation
        evaluated_moves.append((move, fitness))

    return evaluated_moves




def refine_fuzzy_logic_system(board_state, iterations=20):
    best_move = None
    best_fitness = float('-inf')

    for _ in range(iterations):
        # Step 1: Generate and evaluate all possible moves
        evaluated_moves = generate_and_evaluate_moves(board_state)

        # Step 2: Select the best move from the evaluated ones
        evaluated_moves.sort(key=lambda x: x[1], reverse=True)
        current_best_move, current_best_fitness = evaluated_moves[0]

        # Update best move and fitness
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_move = current_best_move

        # Step 3: Adjust the fuzzy logic system based on the best move
        # This can involve tweaking the membership functions or rules slightly
        adjust_fuzzy_logic_system(current_best_move, board_state)

    return best_move



def adjust_fuzzy_logic_system(best_move, board_state):
    # Example adjustment strategy:
    # If a particular fuzzy rule consistently leads to good outcomes, strengthen it.

    piece_advantage_value = calculate_piece_advantage(best_move[2])
    positional_strength_value = calculate_positional_strength(best_move[2])

    # If the best move had a high positional strength, make the "strong" membership function steeper
    if positional_strength_value > 75:
        positional_strength['strong'] = fuzz.trimf(positional_strength.universe, [40, 80, 100])

    # Similarly, adjust rules if they frequently lead to good results
    if piece_advantage_value > 0 and positional_strength_value > 50:
        # Strengthen the influence of this rule
        rule6 = ctrl.Rule(piece_advantage['medium'] & positional_strength['strong'], evaluation['excellent'])

    # Rebuild the control system with the adjusted rules
    evaluation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    evaluation_sim = ctrl.ControlSystemSimulation(evaluation_ctrl)




def fuzzy_logic_based_move_selection(board_state, iterations=20):
    best_move = refine_fuzzy_logic_system(board_state, iterations)
    return best_move

'''



def generate_possible_moves(board_state, ai_piece=1, opponent_piece=-1):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 
    capture_directions = [(2 * d[0], 2 * d[1]) for d in directions] 

    def is_within_bounds(x, y):
        return 0 <= x < board_state.shape[0] and 0 <= y < board_state.shape[1]

    possible_moves = []

    for i in range(board_state.shape[0]):
        for j in range(board_state.shape[1]):
            if board_state[i, j] == ai_piece:
                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if is_within_bounds(new_i, new_j) and board_state[new_i, new_j] == 0:
                        new_board = board_state.copy()
                        new_board[i, j] = 0
                        new_board[new_i, new_j] = ai_piece
                        move = ((i, j), (new_i, new_j), new_board)
                        possible_moves.append(move)
                for capture_direction in capture_directions:
                    mid_i, mid_j = i + capture_direction[0] // 2, j + capture_direction[1] // 2
                    new_i, new_j = i + capture_direction[0], j + capture_direction[1]
                    if (
                        is_within_bounds(mid_i, mid_j) and is_within_bounds(new_i, new_j) and
                        board_state[mid_i, mid_j] == opponent_piece and board_state[new_i, new_j] == 0
                    ):
                        new_board = board_state.copy()
                        new_board[i, j] = 0
                        new_board[mid_i, mid_j] = 0
                        new_board[new_i, new_j] = ai_piece
                        move = ((i, j), (new_i, new_j), new_board)
                        possible_moves.append(move)

    return possible_moves

def calculate_fitness(board, original_board):
    ai_piece = 1
    opponent_piece = -1
    fitness = 0

    original_opponent_pieces = np.sum(original_board == opponent_piece)
    new_opponent_pieces = np.sum(board == opponent_piece)
    captured_pieces = original_opponent_pieces - new_opponent_pieces
    fitness += captured_pieces * 10

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == ai_piece:
                
                fitness += (board.shape[0] - i) * 1
                
                if 2 <= i <= 5 and 2 <= j <= 5:
                    fitness += 2

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == ai_piece:
                for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if 0 <= i + di < board.shape[0] and 0 <= j + dj < board.shape[1]:
                        if board[i + di, j + dj] == opponent_piece:
                            if 0 <= i - di < board.shape[0] and 0 <= j - dj < board.shape[1] and board[i - di, j - dj] == 0:
                                fitness -= 5

   
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == ai_piece:
                for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if 0 <= i + di < board.shape[0] and 0 <= j + dj < board.shape[1]:
                        if board[i + di, j + dj] == 0:
                            fitness += 1

    return fitness


def rank_selection(moves_with_fitness, num_selections):
    
    sorted_moves = sorted(moves_with_fitness, key=lambda x: x[1], reverse=True)
    total_rank = sum(range(1, len(sorted_moves) + 1))
    rank_probabilities = [(rank + 1) / total_rank for rank in range(len(sorted_moves))]
    
   
    cumulative_probabilities = np.cumsum(rank_probabilities)

    
    selected_moves = []
    for _ in range(num_selections):
        r = random.random()
        for i, cumulative_probability in enumerate(cumulative_probabilities):
            if r <= cumulative_probability:
                selected_moves.append(sorted_moves[i][0])
                break

    return selected_moves

def crossover_binary(bin1, bin2):
    crossover_point = random.randint(1, len(bin1) - 1)
    offspring1 = bin1[:crossover_point] + bin2[crossover_point:]
    offspring2 = bin2[:crossover_point] + bin1[crossover_point:]
    return offspring1, offspring2


def mutate_binary(bin_str, mutation_rate=0.01):
    bin_list = list(bin_str)
    for i in range(len(bin_list)):
        if random.random() < mutation_rate:
            bin_list[i] = '1' if bin_list[i] == '0' else '0'
    return ''.join(bin_list)

# Main Fuzzy Logic algorithm function
def fuzzylogic_algorithm_move(board_state):
    best_move = None
    best_fitness = float('-inf')

    iterations = 0
    max_iterations = 20

    while iterations < max_iterations:
        iterations += 1
        possible_moves = generate_possible_moves(board_state)


        if not possible_moves:
            print("No possible moves available. Terminating.")
            break

        if len(possible_moves) == 1:
            best_move = possible_moves[0]
            best_fitness = calculate_fitness(best_move[2], board_state)
            print("Only one possible move available. Terminating.")
            break

        fitness_array = []
        moves_with_fitness = []

        for move in possible_moves:
            fitness = calculate_fitness(move[2], board_state)
            fitness_array.append(fitness)
            moves_with_fitness.append((move, fitness))

        selected_population_1 = rank_selection(moves_with_fitness, 2)

        selected_indices = []
        for move in selected_population_1:
            index = possible_moves.index(move)
            selected_indices.append(index)

        max_index = len(possible_moves) - 1
        bit_length = len(bin(max_index)[2:]) 
        binary_indices = [bin(index)[2:].zfill(bit_length) for index in selected_indices]

        while True:
            offspring1, offspring2 = crossover_binary(binary_indices[0], binary_indices[1])
            offspring1 = mutate_binary(offspring1)
            offspring2 = mutate_binary(offspring2)

            offspring_indices = [int(offspring1, 2), int(offspring2, 2)]
            if all(index <= max_index for index in offspring_indices):
                break

        offspring_moves = [possible_moves[index] for index in offspring_indices]

        for move in offspring_moves:
            fitness = calculate_fitness(move[2], board_state)
            if fitness > best_fitness:
                best_fitness = fitness
                best_move = move

    return best_move
