import pygame
import numpy as np
import time  # Import time module for delay

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("แดนอบาย888")

# Load background image
slot_black = pygame.image.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\3.png").convert_alpha()

def draw_background():
    back_size = pygame.transform.scale(slot_black, (screen_width, screen_height))
    screen.blit(back_size, (0, 0))

# Initialize fonts
font = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 20)
font1 = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 40)  # Larger font for icons

# Define the IconLocation class (now for larger text)
class IconLocation:
    def __init__(self, pos_x, pos_y, text):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text_surface = font1.render(text, True, (74, 19, 15))  # Use font1

    def set_text(self, text):
        self.text = text
        self.text_surface = font1.render(text, True, (74, 19, 15))  # Use font1

    def draw(self, screen):
        text_rect = self.text_surface.get_rect(center=(self.pos_x + 75, self.pos_y + 100))  # Center text in the icon area
        screen.blit(self.text_surface, text_rect)

def get_start():
    global rand_icon, show_icons
    rand_icon = np.random.choice(icon, 3, p=icon_prob)
    loc_left.set_text(rand_icon[0])
    loc_middle.set_text(rand_icon[1])
    loc_right.set_text(rand_icon[2])
    show_icons = True  # Set to True to display icons before reward

def reward():
    global credits, reward_text, reward_displayed, total_time_text
    if rand_icon[0] == rand_icon[1] == rand_icon[2]:
        credit = icon_reward[rand_icon[0]]
        credits += credit
        reward_text = font.render(f'You get {credit} hours', True, (192, 192, 192))
        total_time_text = font.render(f'You only have {credits} hours left', True, (192, 192, 192))
        reward_displayed = True
    else:
        reward_text = None
        reward_displayed = False

# Define icons and probabilities
icon = ["Nails", "hair", "Arrow", "Nanartong", "Guman"]
icon_prob = [0.30, 0.25, 0.20, 0.15, 0.10]  # Fixed probabilities to sum to 1
icon_reward = {
    "Nails": -20,
    "hair": -50,
    "Arrow": +10,
    "Guman": +250,
    "Nanartong": +730,
}

# Calculate positions with padding
padding = 80  # Space between icons
icon_width, icon_height = 150, 200
total_width = 3 * icon_width + 2 * padding
start_x = (screen_width - total_width) // 2.05
height_location = (screen_height - icon_height)//1.80

# Create IconLocation instances with padding
loc_left = IconLocation(start_x, height_location, "Nails")
loc_middle = IconLocation(start_x + icon_width + padding, height_location, "hair")
loc_right = IconLocation(start_x + 2 * (icon_width + padding), height_location, "Nanartong")

# Player life
credits = 1000

# Initialize reward text
reward_text = None
reward_displayed = False
total_time_text = None
show_icons = False

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if credits >= 10:
                    credits -= 10  # Deduct 10 credits each round
                    get_start()  # Update icons

    # Clear the screen
    draw_background()

    # Draw the text icons
    loc_left.draw(screen)
    loc_middle.draw(screen)
    loc_right.draw(screen)

    # Render credits text
    days = credits / 24
    pygame.draw.rect(screen, (188, 159, 124), (screen_width//2-150, 20, 300, 50), width=0)
    text = font.render(f'Hours: {credits} = {days:.2f} DAYS', True, (80, 26, 31))
    text_rect = text.get_rect(center=((screen_width//2, 50)))  # Position text at the top
    screen.blit(text, text_rect)

    pygame.display.flip()  # Update the display

    if show_icons:
        time.sleep(0.5)  # Show icons for 0.5 seconds
        reward()  # Calculate reward
        show_icons = False

    if reward_displayed:
        # Clear the screen to black and display reward text
        screen.fill((0, 0, 0))
        if reward_text:
            reward_text_rect = reward_text.get_rect(center=(screen_width // 2, screen_height // 2 - 20))
            screen.blit(reward_text, reward_text_rect)
        if total_time_text:
            total_time_text_rect = total_time_text.get_rect(center=(screen_width // 2, screen_height // 2 + 20))
            screen.blit(total_time_text, total_time_text_rect)
        pygame.display.flip()
        time.sleep(1)  # Show the reward message for 1 second
        reward_displayed = False

pygame.quit()
