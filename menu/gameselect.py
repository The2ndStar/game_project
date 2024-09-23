import pygame
import os
import sys 
sys.path.append(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project')
from gameplay.slot import slot

def gameselect(screen):
    pygame.init()

    screen_width = 800
    screen_height = 500

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("แดนอบาย888")

    # Load the background image and scale it to fit the screen
    background_image = pygame.image.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\5.png").convert_alpha()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Define positions for the three images
    image_width = 150
    image_height = 100
    spacing = (screen_width - 3 * image_width) // 2.15  # Space between images

    image_positions = [
        (spacing, (screen_height - image_height) // 1.075),  # Position 1
        ((spacing * 2) + 85, (screen_height - image_height) // 1.075),  # Position 2
        ((spacing * 4) - 15, (screen_height - image_height) // 1.075)  # Position 3
    ]

    # Color definitions
    color_game = (56, 12, 8)

    # Initialize fonts
    font_game = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 25)

    # Render text
    slot_text = font_game.render("Slot Machine", True, color_game)
    High_Low_text = font_game.render("High-Low", True, color_game)
    IDK_text = font_game.render("smt", True, color_game)

    # Create rects for the text (for collision detection)
    slot_rect = slot_text.get_rect(center=image_positions[0])
    high_low_rect = High_Low_text.get_rect(center=image_positions[1])
    idk_rect = IDK_text.get_rect(center=image_positions[2])

    # Main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if slot_rect.collidepoint(mouse_pos):
                    slot(screen)  # Call slot game function
                elif high_low_rect.collidepoint(mouse_pos):
                    screen.fill((0, 0, 0))  # Example action for High-Low
                elif idk_rect.collidepoint(mouse_pos):
                    screen.fill((255, 255, 255))  # Example action for smt (IDK)

            if event.type == pygame.QUIT:
                run = False
                return

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the text/buttons on top of the background
        screen.blit(slot_text, slot_rect)
        screen.blit(High_Low_text, high_low_rect)
        screen.blit(IDK_text, idk_rect)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    return True
