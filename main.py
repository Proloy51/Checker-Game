import pygame
import sys
import numpy as np
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minmax.algorithm import minimax
from checkers.board import Board
from genetic.genetic_algo import genetic_algorithm_move  
from Fuzzy_Logic.fuzzy_logic import generate_possible_moves

FPS = 60

pygame.init()
pygame.font.init()


MOVE_WIDTH = 300 
TOTAL_WIDTH = WIDTH + MOVE_WIDTH

WIN = pygame.display.set_mode((TOTAL_WIDTH, HEIGHT))
pygame.display.set_caption('Checker Board')


game_surface = pygame.Surface((WIDTH, HEIGHT))
move_surface = pygame.Surface((MOVE_WIDTH, HEIGHT))

def draw_text(surface, text, font, color, rect):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def main_menu():
    menu = True
    font = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 50)
    
    button_width = 300
    button_height = 60

    while menu:
        WIN.fill((0, 0, 0))
        
        new_game_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 3, button_width, button_height)
        leaderboard_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)
        exit_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, 2 * HEIGHT // 3, button_width, button_height)
        
        mouse_pos = pygame.mouse.get_pos()
        if new_game_button.collidepoint(mouse_pos):
            new_game_color = (255, 255, 255)  
            new_game_text_color = (0, 200, 0)  
        else:
            new_game_color = (0, 200, 0)  
            new_game_text_color = (255, 255, 255) 
        
        if leaderboard_button.collidepoint(mouse_pos):
            leaderboard_color = (255, 255, 255)  
            leaderboard_text_color = (0, 200, 0)  
        else:
            leaderboard_color = (0, 200, 0)  
            leaderboard_text_color = (255, 255, 255)  
        
        if exit_button.collidepoint(mouse_pos):
            exit_color = (255, 255, 255)  
            exit_text_color = (0, 200, 0)  
        else:
            exit_color = (0, 200, 0)  
            exit_text_color = (255, 255, 255)  
        
        pygame.draw.rect(WIN, new_game_color, new_game_button)
        pygame.draw.rect(WIN, leaderboard_color, leaderboard_button)
        pygame.draw.rect(WIN, exit_color, exit_button)
        
        draw_text(WIN, 'Checkers', font, (255, 255, 255), pygame.Rect(TOTAL_WIDTH // 2 - 100, HEIGHT // 6, 200, 50))
    
        draw_text(WIN, 'New Game', font_small, new_game_text_color, new_game_button)
        draw_text(WIN, 'Leaderboard', font_small, leaderboard_text_color, leaderboard_button)
        draw_text(WIN, 'Exit', font_small, exit_text_color, exit_button)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), new_game_button) 
                    draw_text(WIN, 'New Game', font_small, (0, 200, 0), new_game_button) 
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    method_menu() 
                    menu = False
                elif leaderboard_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), leaderboard_button) 
                    draw_text(WIN, 'Leaderboard', font_small, (0, 200, 0), leaderboard_button)  
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    pass  
                elif exit_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), exit_button)  
                    draw_text(WIN, 'Exit', font_small, (0, 200, 0), exit_button)
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    pygame.quit()
                    sys.exit()

def method_menu():
    menu = True
    font = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 50)
    font_medium = pygame.font.Font(None, 60)
    
    button_width = 300
    button_height = 60

    while menu:
        WIN.fill((0, 0, 0))
        
        prompt_text_rect = pygame.Rect(TOTAL_WIDTH // 2 - 200, HEIGHT // 6, 400, 50)

        alpha_minimax_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 3, button_width, button_height)
        genetic_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)
        fuzzylogic_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 2 + button_height + 60, button_width, button_height)
        

        mouse_pos = pygame.mouse.get_pos()
        if alpha_minimax_button.collidepoint(mouse_pos):
            alpha_minimax_color = (255, 255, 255) 
            alpha_minimax_text_color = (0, 200, 0) 
        else:
            alpha_minimax_color = (0, 200, 0)  
            alpha_minimax_text_color = (255, 255, 255)  
        
        if genetic_button.collidepoint(mouse_pos):
            genetic_color = (255, 255, 255) 
            genetic_text_color = (0, 200, 0)  
        else:
            genetic_color = (0, 200, 0)  
            genetic_text_color = (255, 255, 255) 
            
        if fuzzylogic_button.collidepoint(mouse_pos):
            fuzzylogic_color = (255, 255, 255) 
            fuzzylogic_text_color = (0, 200, 0) 
        else:
            fuzzylogic_color = (0, 200, 0)  
            fuzzylogic_text_color = (255, 255, 255) 
        
  
        draw_text(WIN, 'Which method to use?', font_medium, (255, 255, 255), prompt_text_rect)
        
        pygame.draw.rect(WIN, alpha_minimax_color, alpha_minimax_button)
        pygame.draw.rect(WIN, genetic_color, genetic_button)
        pygame.draw.rect(WIN, fuzzylogic_color, fuzzylogic_button)
        
        draw_text(WIN, 'AlphaMnMx', font_small, alpha_minimax_text_color, alpha_minimax_button)
        draw_text(WIN, 'Genetic', font_small, genetic_text_color, genetic_button)
        draw_text(WIN, 'Fuzzy Logic', font_small, fuzzylogic_text_color, fuzzylogic_button)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if alpha_minimax_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), alpha_minimax_button) 
                    draw_text(WIN, 'AlphaMnMx', font_small, (0, 200, 0), alpha_minimax_button)  
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    menu = False
                    difficulty_menu('alpha_minimax') 
                elif genetic_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), genetic_button)  
                    draw_text(WIN, 'Genetic', font_small, (0, 200, 0), genetic_button)  
                    pygame.display.flip()
                    pygame.time.wait(200) 
                    menu = False
                    main(0, 'genetic')  
                    
                elif fuzzylogic_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), fuzzylogic_button)  
                    draw_text(WIN, 'Fuzzy Logic', font_small, (0, 200, 0), fuzzylogic_button) 
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    menu = False
                    main(0, 'Fuzzy Logic') 

def difficulty_menu(selected_algorithm):
    menu = True
    font = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 50)
    
    button_width = 300
    button_height = 60

    while menu:
        WIN.fill((0, 0, 0))
        
        easy_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 3, button_width, button_height)
        medium_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)
        hard_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, 2 * HEIGHT // 3, button_width, button_height)
        
        mouse_pos = pygame.mouse.get_pos()
        if easy_button.collidepoint(mouse_pos):
            easy_color = (255, 255, 255)  
            easy_text_color = (0, 200, 0)  
        else:
            easy_color = (0, 200, 0)  
            easy_text_color = (255, 255, 255)  
        
        if medium_button.collidepoint(mouse_pos):
            medium_color = (255, 255, 255) 
            medium_text_color = (0, 200, 0)  
        else:
            medium_color = (0, 200, 0)  
            medium_text_color = (255, 255, 255)  
        
        if hard_button.collidepoint(mouse_pos):
            hard_color = (255, 255, 255) 
            hard_text_color = (0, 200, 0)  
        else:
            hard_color = (0, 200, 0)  
            hard_text_color = (255, 255, 255)  
        
        pygame.draw.rect(WIN, easy_color, easy_button)
        pygame.draw.rect(WIN, medium_color, medium_button)
        pygame.draw.rect(WIN, hard_color, hard_button)
        
        draw_text(WIN, 'Easy', font_small, easy_text_color, easy_button)
        draw_text(WIN, 'Medium', font_small, medium_text_color, medium_button)
        draw_text(WIN, 'Hard', font_small, hard_text_color, hard_button)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), easy_button)  
                    draw_text(WIN, 'Easy', font_small, (0, 200, 0), easy_button)  
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    menu = False
                    main(3, selected_algorithm)  
                elif medium_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), medium_button)  
                    draw_text(WIN, 'Medium', font_small, (0, 200, 0), medium_button) 
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    menu = False
                    main(4, selected_algorithm)  
                elif hard_button.collidepoint(event.pos):
                    pygame.draw.rect(WIN, (255, 255, 255), hard_button)  
                    draw_text(WIN, 'Hard', font_small, (0, 200, 0), hard_button)  
                    pygame.display.flip()
                    pygame.time.wait(200)  
                    menu = False
                    main(5, selected_algorithm)  

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def display_moves(game, font, font_small):
    move_surface.fill((50, 50, 50)) 
    player_moves_text = f"Player Moves: {game.player_moves}"
    ai_moves_text = f"AI Moves: {game.ai_moves}"
    player_moves_surface = font.render(player_moves_text, True, (255, 255, 255))
    ai_moves_surface = font.render(ai_moves_text, True, (255, 255, 255))
    move_surface.blit(player_moves_surface, (20, 50))
    move_surface.blit(ai_moves_surface, (20, 100))
    
    button_width = 200
    button_height = 60
    return_button = pygame.Rect(50, HEIGHT - 150, button_width, button_height)
    restart_button = pygame.Rect(50, HEIGHT - 70, button_width, button_height)
    

    mouse_pos = pygame.mouse.get_pos()
    

    if return_button.collidepoint(mouse_pos):
        return_button_color = (255, 255, 255)  
        return_text_color = (255, 0, 0)  
    else:
        return_button_color = (255, 255, 255)  
        return_text_color = (0, 0, 0)  
    
    if restart_button.collidepoint(mouse_pos):
        restart_button_color = (255, 255, 255)  
        restart_text_color = (255, 0, 0)  
    else:
        restart_button_color = (255, 255, 255)  
        restart_text_color = (0, 0, 0)  
    
    pygame.draw.rect(move_surface, return_button_color, return_button) 
    pygame.draw.rect(move_surface, restart_button_color, restart_button)  

    draw_text(move_surface, 'Return', font_small, return_text_color, return_button)  
    draw_text(move_surface, 'Restart', font_small, restart_text_color, restart_button) 
    
    
def display_winner_message(winner):
    font_large = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 50)

    if winner == WHITE:
        message = "AI Wins!"
    else:
        message = "Human Wins!"
  
    button_width = 200
    button_height = 60
    button_spacing = 20

    restart_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)
    menu_button = pygame.Rect(TOTAL_WIDTH // 2 - button_width // 2, HEIGHT // 2 + button_height + button_spacing, button_width, button_height)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(pos):
                    main(3, 'alpha_minimax') 
                    return
                elif menu_button.collidepoint(pos):
                    main_menu()
                    return
        
        move_surface.fill((50, 50, 50))
        
        message_rect = pygame.Rect(0, HEIGHT // 4, TOTAL_WIDTH, 100)
        pygame.draw.rect(WIN, (0, 200, 0), message_rect)  

        draw_text(WIN, message, font_large, (255, 255, 255), message_rect)
   
        pygame.draw.rect(WIN, (0, 200, 0), restart_button)
        draw_text(WIN, 'Restart', font_small, (255, 255, 255), restart_button)
        
        pygame.draw.rect(WIN, (0, 200, 0), menu_button)
        draw_text(WIN, 'Main Menu', font_small, (255, 255, 255), menu_button)
        
        pygame.display.flip()

    

def main(difficulty=3, algorithm='alpha_minimax'):
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game(game_surface)

    font = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 50)
    
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            if algorithm == 'alpha_minimax':
                value, new_board = minimax(game.get_board(), difficulty, float('-inf'), float('inf'), True, game)
                
            elif algorithm == 'genetic':
                board_array = game.get_board().to_array()  
                best_move = genetic_algorithm_move(board_array)
                new_board = Board()  
                new_board.from_array(best_move[2])  
                
            elif algorithm == "Fuzzy Logic":
                try:
                    '''# Use fuzzy evaluation
                    best_move = None
                    best_score = float('-inf')
                    
                    # Generate all possible moves and evaluate them
                    for move in game.get_possible_moves():
                        test_board = game.get_board().copy()  # Create a copy of the board
                        test_board.apply_move(move)  # Apply the move to the test board
                        score = fuzzy_evaluate(test_board)  # Evaluate the board with fuzzy logic
                        
                        if score > best_score:
                            best_score = score
                            best_move = move
                    
                    if best_move is not None:
                        new_board = Board()  # Create a new board from the best move
                        new_board.apply_move(best_move)  # Apply the best move to the new board'''
                    
                    board_array = game.get_board().to_array() 
                    best_move = genetic_algorithm_move(board_array)
                    #best_move = fuzzy_logic_based_move_selection(board_array,20)
                    new_board = Board() 
                    new_board.from_array(best_move[2])  
                        
                    #value, new_board = minimax(game.get_board(), 3, float('-inf'), float('inf'), True, game)
                
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    break 

            game.ai_move(new_board)

        winner = game.winner()
        if winner is not None:
            print(winner)
            display_winner_message(winner)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
            
                button_width = 200
                button_height = 60
                return_button = pygame.Rect(WIDTH + 50, HEIGHT - 150, button_width, button_height)
                restart_button = pygame.Rect(WIDTH + 50, HEIGHT - 70, button_width, button_height)
                if return_button.collidepoint(pos):
                    main_menu() 
                    return
                if restart_button.collidepoint(pos):
                    game.reset()
                if pos[0] < WIDTH: 
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        game.update()
        display_moves(game, font, font_small)
        
        WIN.blit(game_surface, (0, 0))
        WIN.blit(move_surface, (WIDTH, 0))
        pygame.display.flip()
    
    pygame.quit()

main_menu()
