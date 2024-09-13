import pygame
import sys
import story.main as main  # Import main.py from the story folder

pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("แดนอบาย888")
start_back = pygame.image.load(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\start_back.png')

def draw_background():
    back_size = pygame.transform.scale(start_back, (screen_width, screen_height))
    screen.blit(back_size, (0, 0))

color_rect = (188,159,124)
color_text = (80,26,31)
rect_option = pygame.Rect(60,55, 200, 50)
rect_save = pygame.Rect(540,55,200,50)
rect_sound = pygame.Rect(60,400,200,50)
rect_exit = pygame.Rect(540,400,200,50)
width = 0

font_start = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 72)
font_menu = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 30)

option_text = font_menu.render("Option",True,color_text)
save_text = font_menu.render("Game save",True,color_text)
sound_text = font_menu.render("Sound setting",True,color_text)
exit_text = font_menu.render("Exit",True,color_text)
start_text = font_start.render("Start", True, color_text)

def start_func():
    text_rect = start_text.get_rect(center=(screen_width//2,screen_height//2))
    screen.blit(start_text, text_rect)
     
def option_func():
    pygame.draw.rect(screen, color_rect, rect_option, width)
    text_rect = option_text.get_rect(center=rect_option.center)
    screen.blit(option_text, text_rect)
    
def save_func():
    pygame.draw.rect(screen, color_rect, rect_save, width)
    text_rect = save_text.get_rect(center=rect_save.center)
    screen.blit(save_text, text_rect)
    
def sound_func():
    pygame.draw.rect(screen, color_rect, rect_sound, width)
    text_rect = sound_text.get_rect(center=rect_sound.center)
    screen.blit(sound_text, text_rect)
    
def exit_func():
    pygame.draw.rect(screen, color_rect, rect_exit, width)
    text_rect = exit_text.get_rect(center=rect_exit.center)
    screen.blit(exit_text, text_rect)
    
def is_point_in_rect(point, rect):
    return rect.collidepoint(point)

game_state = "start_menu"  # Initialize the game state

run = True
while run:
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game_state == "start_menu":
                if is_point_in_rect(mouse_pos, rect_option):
                    print("Option button clicked!")
                elif is_point_in_rect(mouse_pos, rect_save):
                    print("Save button clicked!")
                elif is_point_in_rect(mouse_pos, rect_sound):
                    print("Sound button clicked!")
                elif is_point_in_rect(mouse_pos, rect_exit):
                    print("Exit button clicked!")
                elif is_point_in_rect(mouse_pos, pygame.Rect(start_width//2 - start_text.get_width()//2, screen_height//2 - start_text.get_height()//2, start_text.get_width(), start_text.get_height())):
                    game_state = "main_game"
                    # Call the function to start the main game
                    main.run_game()

        if event.type == pygame.QUIT:
            run = False
    
    draw_background()
    start_func()
    option_func()
    save_func()
    sound_func()
    exit_func()

    pygame.display.flip()

pygame.quit()
