import numpy as np
import random

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

# Main genetic algorithm function
def genetic_algorithm_move(board_state):
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
