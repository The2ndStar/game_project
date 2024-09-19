import pygame
import sys  # Import main.py from the story folder

pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("แดนอบาย888")
start_back = pygame.image.load(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\1.png')

def draw_background():
    back_size = pygame.transform.scale(start_back, (screen_width, screen_height))
    screen.blit(back_size, (0, 0))

pygame.mixer.music.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\sound\Bg_sound.mp3")
pygame.mixer.music.play(-1)  # Play the music in a loop (-1 means loop indefinitely)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_background()  # Draw background in each frame
    pygame.display.flip()  # Update the display

pygame.quit()

