import pygame
from image import mail_pic

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
spacing = (screen_width - 3 * image_width) //2.15  # Space between images

image_positions = [
    (spacing, (screen_height - image_height) // 1.075),  # Position 1
    ((spacing*2)+85, (screen_height - image_height) // 1.075),  # Position 2
    ((spacing *4)-15, (screen_height - image_height) // 1.075)  # Position 3
]

# Color definitions
color_game = (56, 12, 8)
color_text = (56, 12, 8)

# Initialize fonts
font_game = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 25)

# Render text
slot_text = font_game.render("Slot Machine", True, color_game)
High_Low_text = font_game.render("High-Low", True, color_game)
IDK_text = font_game.render("smt", True, color_game)

# Load and resize images

def slot_func():
    text_rect = slot_text.get_rect(center=image_positions[0])
    screen.blit(slot_text, text_rect)

def high_low_func():
    text_rect = High_Low_text.get_rect(center=image_positions[1])
    screen.blit(High_Low_text, text_rect)

def idk_func():
    text_rect = IDK_text.get_rect(center=image_positions[2])
    screen.blit(IDK_text, text_rect)

def is_point_in_rect(point, rect):
    return rect.collidepoint(point)

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            # Check which image was clicked
            for i, pos in enumerate(image_positions):
                if pygame.Rect(pos, (image_width, image_height)).collidepoint(mouse_pos):
                    if i == 0:
                        print("Slot Machine image clicked!")
                    elif i == 1:
                        print("High-Low image clicked!")
                    elif i == 2:
                        print("IDK image clicked!")

        if event.type == pygame.QUIT:
            run = False

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the text
    slot_func()
    high_low_func()
    idk_func()

    pygame.display.flip()

pygame.quit()
