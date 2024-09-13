import pygame
from image import mail_pic

pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("แดนอบาย888")

# Define positions for the three images
image_width = 150
image_height = 100
# Define rectangle sizes and positions, placing them below each image
rect_width = 200
rect_height = 30
rect_spacing = 50

#color
color_bg = (188,159,124)
color_game =  (195,181,146)
color_text = (80,26,31)
color_rect = (51,10,9)
screen.fill(color_bg)

font_sec = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\MATURASC.TTF', 54)
sec_text = font_sec.render("What do you want to paly ?", True, color_text)

font_game = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 25)

slot_text = font_game.render("Slot Machine",True,color_game)
High_Low_text = font_game.render("High-Low",True,color_game)
IDK_text = font_game.render("smt",True,color_game)


spacing = (screen_width - 3 * image_width) // 4  # Space between images

image_positions = [
    (spacing, (screen_height - image_height) // 2),  # Position 1
    (spacing + image_width + spacing, (screen_height - image_height) // 2),  # Position 2
    (spacing + 2 * (image_width + spacing), (screen_height - image_height) // 2)  # Position 3
]

# Define rectangle positions
rect_slot = pygame.Rect(image_positions[0][0]-25, image_positions[0][1] + image_height + rect_spacing, rect_width, rect_height)
rect_Highlow = pygame.Rect(image_positions[1][0]-25, image_positions[1][1] + image_height + rect_spacing, rect_width, rect_height)
rect_idk = pygame.Rect(image_positions[2][0]-25, image_positions[2][1] + image_height + rect_spacing, rect_width, rect_height)

# Define fonts and render text

def sec_func():
    text_rect = sec_text.get_rect(center=(screen_width // 2, screen_height // 5.5))
    screen.blit(sec_text, text_rect)

def slot_func():
    text_rect = slot_text.get_rect(center=rect_slot.center)
    screen.blit(slot_text, text_rect)

def high_low_func():
    text_rect = High_Low_text.get_rect(center=rect_Highlow.center)
    screen.blit(High_Low_text, text_rect)

def idk_func():
    text_rect = IDK_text.get_rect(center=rect_idk.center)
    screen.blit(IDK_text, text_rect)

# Load and resize images
image = mail_pic()
if image is not None:
    resized_image = pygame.transform.scale(image, (150, 100))

# Define positions for the three images
image_width = 150
image_height = 100
spacing = (screen_width - 3 * image_width) // 4  # Space between images


image_positions = [
    (spacing, (screen_height - image_height) // 2),  # Position 1
    (spacing + image_width + spacing, (screen_height - image_height) // 2),  # Position 2
    (spacing + 2 * (image_width + spacing), (screen_height - image_height) // 2)  # Position 3
]

def is_point_in_rect(point, rect):
    return rect.collidepoint(point)

run = True
while run:
    
     for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if is_point_in_rect(mouse_pos, rect_slot):
                print("Slot button clicked!")
            elif is_point_in_rect(mouse_pos, rect_Highlow):
                print("High-Low button clicked!")
            elif is_point_in_rect(mouse_pos, rect_idk):
                print("IDK button clicked!")

        if event.type == pygame.QUIT:
            run = False
            
     if resized_image is not None:
        for pos in image_positions:
            screen.blit(resized_image, pos)

    # Draw the rectangles
     pygame.draw.rect(screen, color_rect, rect_slot)
     pygame.draw.rect(screen, color_rect, rect_Highlow)
     pygame.draw.rect(screen, color_rect, rect_idk)

    # Draw the text inside the rectangles
     sec_func()
     slot_func()
     high_low_func()
     idk_func()

     pygame.display.flip()

pygame.quit()
