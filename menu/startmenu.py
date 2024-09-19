import os
import pygame
import time

def Start(screen):
    screen_width = 800
    screen_height = 500

    start_back = pygame.image.load(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\1.png')

    def draw_background():
        back_size = pygame.transform.scale(start_back, (screen_width, screen_height))
        screen.blit(back_size, (0, 0))

    pygame.mixer.music.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\sound\Bg_sound.mp3")
    pygame.mixer.music.play(-1)  # Play the music in a loop (-1 means loop indefinitely)

    start_time = time.time()  # Record the start time
    delay = 3 # 10-second delay before transitioning

    run = True
    while run:
        current_time = time.time()
        if current_time - start_time > delay:
            return True  # Automatically transition to the next page after 10 seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit to the main loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True  # Proceed to the next page

        draw_background()
        pygame.display.flip()  # Update the display

    return True

