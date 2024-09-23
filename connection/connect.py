import sys
import os
import pygame

# Add the root directory to sys.path so Python can find 'menu' and 'story' folders
sys.path.append(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project')

from menu.startmenu import Start
from story.main import Story

pygame.init()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Page Navigation")

def main():
    # Display the Start page
    if not Start(screen):
        pygame.quit()
        return
    
    # Display the Story pages
    if not Story(screen):
        pygame.quit()
        return

    
    pygame.quit()

if __name__ == "__main__":
    main()
