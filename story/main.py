import pygame
import sys
import pygame_gui
pygame.init()

screen_width = 800
screen_height = 500

color_text = (255, 255, 255)
color_rect = (188,159,124)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("แดนอบาย888")
bg_story1 = pygame.image.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\4.png").convert_alpha()
font_menu = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 30)

def draw_background():
    back_size = pygame.transform.scale(bg_story1, (screen_width, screen_height))
    screen.blit(back_size, (0, 0))

def page1():
    draw_background()
    welcome_text1 = font_menu.render('warmly welcome lost gambler', True, color_text)
    welcome_text2 = font_menu.render('We are waiting for you', True, color_text)
    screen.blit(welcome_text1, ((screen_width / 4) + 20, (screen_height / 3) + 15))
    screen.blit(welcome_text2, ((screen_width / 4) + 50, (screen_height / 2) + 15))

def page2():
    screen.fill((0, 0, 0))  # Clear the screen with black color
    textq1 = font_menu.render('You arrived', True, color_text)
    screen.blit(textq1, ((screen_width /2)-90, (screen_height /2)-10))

def page3():
    draw_background()  # Show the background
    Clock = pygame.time.Clock()
    Manager = pygame_gui.UIManager((screen_width, screen_height))

    # Render the question above the input box
    q1 = font_menu.render('Well, who are you then?', True, color_text)
    text_rect = q1.get_rect(center=(screen_width // 2, (screen_height // 2) - 75))  # Positioned above input box

    # Define the input box dimensions
    rect_x, rect_y = screen_width // 2 - 150, screen_height // 2
    rect_width, rect_height = 300, 50

    # Create a text input line, with no background (transparent)
    TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((rect_x, rect_y), (rect_width, rect_height)),
        manager=Manager
    )

    user_input = ""  # Store user input
    input_finished = False  # Flag to check if input is done
    running = True
    timer_started = False  # Timer for flipping page after input

    while running:
        UI_refresh = Clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            Manager.process_events(event)

            # Handle input submission
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == TEXT_INPUT:
                user_input = event.text  # Capture the input text
                input_finished = True  # Set flag when input is done
                timer_started = pygame.time.get_ticks()  # Start timer to flip the page

        Manager.update(UI_refresh)
        draw_background()  # Redraw the background for smooth UI update

        # Draw the question text
        screen.blit(q1, text_rect.topleft)

        # Draw the filled rectangle for the input box with 'color_rect'
        pygame.draw.rect(screen, color_rect, (rect_x, rect_y, rect_width, rect_height))  # Filled rectangle

        # Draw the text input field (no need for a separate rectangle border)
        Manager.draw_ui(screen)

        # If the input is finished, display the follow-up text
        if input_finished:
            textq2 = font_menu.render(f"Nice to meet you, {user_input}!", True, color_text)
            screen.blit(textq2, ((screen_width // 2) - 150, (screen_height // 2) + 70))  # Positioned below input

            # After showing the text, wait for 2 seconds then flip to page 4
            if pygame.time.get_ticks() - timer_started > 2000:  # 2 seconds delay
                page4()  # Call the next page function

        pygame.display.update()

def page4():
    draw_background()  # Show the background
    q2 = font_menu.render('How long did you Advent?', True, color_text)
    
    text_rect = q2.get_rect(center=(screen_width // 2, (screen_height // 2)-15))
    rect_width = 300  # Adjusted width to fit the text
    rect_height = 50

    rect_x = text_rect.centerx - (rect_width // 2)
    rect_y = text_rect.bottom + 10  # Position the rectangle 10 pixels below the text
    rect_q1 = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    
    pygame.draw.rect(screen, color_rect, rect_q1)
    
    screen.blit(q2, text_rect.topleft)
     draw_background()  # Show the background
    Clock = pygame.time.Clock()
    Manager = pygame_gui.UIManager((screen_width, screen_height))

    # Render the question above the input box
    q1 = font_menu.render('Well, who are you then?', True, color_text)
    text_rect = q1.get_rect(center=(screen_width // 2, (screen_height // 2) - 75))  # Positioned above input box

    # Define the input box dimensions
    rect_x, rect_y = screen_width // 2 - 150, screen_height // 2
    rect_width, rect_height = 300, 50

    # Create a text input line, with no background (transparent)
    TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((rect_x, rect_y), (rect_width, rect_height)),
        manager=Manager
    )

    user_input = ""  # Store user input
    input_finished = False  # Flag to check if input is done
    running = True
    timer_started = False  # Timer for flipping page after input

    while running:
        UI_refresh = Clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            Manager.process_events(event)

            # Handle input submission
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == TEXT_INPUT:
                user_input = event.text  # Capture the input text
                input_finished = True  # Set flag when input is done
                timer_started = pygame.time.get_ticks()  # Start timer to flip the page

        Manager.update(UI_refresh)
        draw_background()  # Redraw the background for smooth UI update

        # Draw the question text
        screen.blit(q1, text_rect.topleft)

        # Draw the filled rectangle for the input box with 'color_rect'
        pygame.draw.rect(screen, color_rect, (rect_x, rect_y, rect_width, rect_height))  # Filled rectangle

        # Draw the text input field (no need for a separate rectangle border)
        Manager.draw_ui(screen)

        # If the input is finished, display the follow-up text
        if input_finished:
            textq2 = font_menu.render(f"Nice to meet you, {user_input}!", True, color_text)
            screen.blit(textq2, ((screen_width // 2) - 150, (screen_height // 2) + 70))  # Positioned below input

            # After showing the text, wait for 2 seconds then flip to page 4
            if pygame.time.get_ticks() - timer_started > 2000:  # 2 seconds delay
                page4()  # Call the next page function

        pygame.display.update()

def page5():
    draw_background()  # Show the background
    q3 = font_menu.render('Do you want to play this game?', True, color_text)
    
    # Position the question text
    text_rect = q3.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the rectangle behind the text
    rect_width = 300
    rect_height = 50
    rect_x = text_rect.centerx - (rect_width // 2)
    rect_y = text_rect.bottom + 10

    
    # Draw the question text
    screen.blit(q3, text_rect.topleft)
    
    # Draw "Yes" and "No" buttons
    button_width = 100
    button_height = 40
    
    # Center the buttons below the text
    total_buttons_width = button_width * 2 + 20  # Add space between buttons
    buttons_x = text_rect.centerx - (total_buttons_width // 2)
    
    yes_button_rect = pygame.Rect(buttons_x, rect_y , button_width, button_height)
    no_button_rect = pygame.Rect(buttons_x + button_width + 20, rect_y , button_width, button_height)
    
    pygame.draw.rect(screen, color_rect, yes_button_rect)
    pygame.draw.rect(screen, color_rect, no_button_rect)
    
    yes_text = font_menu.render('Yes', True, color_text)
    no_text = font_menu.render('No', True, color_text)
    
    # Center the text inside the buttons
    screen.blit(yes_text, yes_button_rect.move((button_width - yes_text.get_width()) // 2, (button_height - yes_text.get_height()) // 2))
    screen.blit(no_text, no_button_rect.move((button_width - no_text.get_width()) // 2, (button_height - no_text.get_height()) // 2))

def page6():
    draw_background()  # Show the background
    q5 = font_menu.render('What about your loved one?', True, color_text)
    
    # Position the question text
    text_rect = q5.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the question text
    screen.blit(q5, text_rect.topleft)
    
    # Draw "Yes", "I do not know", and "No" buttons
    button_texts = ['of course', 'I do not know', 'No']  # Swapped "No" and "I do not know"
    button_widths = []
    button_heights = []
    button_rects = []
    
    for text in button_texts:
        text_surf = font_menu.render(text, True, color_text)
        button_widths.append(text_surf.get_width() + 20)  # Adding padding
        button_heights.append(text_surf.get_height() + 10)  # Adding padding
    
    total_buttons_width = sum(button_widths) + 20 * (len(button_texts) - 1)  # Space between buttons
    buttons_x = text_rect.centerx - (total_buttons_width // 2)
    buttons_y = text_rect.bottom + 20  # Adjust this value to position buttons
    
    # Create button rectangles
    for i, (text, width, height) in enumerate(zip(button_texts, button_widths, button_heights)):
        rect = pygame.Rect(buttons_x, buttons_y, width, height)
        button_rects.append(rect)
        buttons_x += width + 20  # Move x position for next button

    # Draw rectangles and text
    for rect, text in zip(button_rects, button_texts):
        pygame.draw.rect(screen, color_rect, rect)
        text_surf = font_menu.render(text, True, color_text)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect.topleft)

def page7():
    draw_background()  # Show the background
    q6 = font_menu.render('Who is the most important to you?', True, color_text)
    
    # Position the question text
    text_rect = q6.get_rect(center=(screen_width // 2, (screen_height // 2.5)))
    
    # Draw the question text
    screen.blit(q6, text_rect.topleft)
    
    # Button texts divided into two rows
    button_texts_row1 = ['Family', 'Friends', 'Lover']
    button_texts_row2 = ['Pet', 'Yourself']
    
    button_widths_row1 = []
    button_heights_row1 = []
    button_rects_row1 = []
    
    button_widths_row2 = []
    button_heights_row2 = []
    button_rects_row2 = []
    
    # Calculate button sizes for row 1
    for text in button_texts_row1:
        text_surf = font_menu.render(text, True, color_text)
        button_widths_row1.append(text_surf.get_width() + 20)  # Adding padding
        button_heights_row1.append(text_surf.get_height() + 10)  # Adding padding
    
    # Calculate button sizes for row 2
    for text in button_texts_row2:
        text_surf = font_menu.render(text, True, color_text)
        button_widths_row2.append(text_surf.get_width() + 20)  # Adding padding
        button_heights_row2.append(text_surf.get_height() + 10)  # Adding padding
    
    # Calculate total width and initial x positions for both rows
    total_buttons_width_row1 = sum(button_widths_row1) + 20 * (len(button_texts_row1) - 1)  # Space between buttons
    total_buttons_width_row2 = sum(button_widths_row2) + 20 * (len(button_texts_row2) - 1)
    
    buttons_x_row1 = text_rect.centerx - (total_buttons_width_row1 // 2)
    buttons_x_row2 = text_rect.centerx - (total_buttons_width_row2 // 2)
    
    # Explicitly set Y positions
    buttons_y_row1 = text_rect.bottom + 20  # Ensure there's enough space
    buttons_y_row2 = buttons_y_row1 + max(button_heights_row1) + 30  # Ensure it's below row 1
    
    # Create and draw button rectangles for row 1
    for i, (text, width, height) in enumerate(zip(button_texts_row1, button_widths_row1, button_heights_row1)):
        rect = pygame.Rect(buttons_x_row1, buttons_y_row1, width, height)
        button_rects_row1.append(rect)
        pygame.draw.rect(screen, color_rect, rect)
        text_surf = font_menu.render(text, True, color_text)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect.topleft)
        buttons_x_row1 += width + 20  # Move x position for next button
    
    # Create and draw button rectangles for row 2
    for i, (text, width, height) in enumerate(zip(button_texts_row2, button_widths_row2, button_heights_row2)):
        rect = pygame.Rect(buttons_x_row2, buttons_y_row2, width, height)
        button_rects_row2.append(rect)
        pygame.draw.rect(screen, color_rect, rect)
        text_surf = font_menu.render(text, True, color_text)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect.topleft)
        buttons_x_row2 += width + 20  # Move x position for next button

    # Update the display
    pygame.display.flip()

def page8():
    draw_background()  # Show the background
    q7 = font_menu.render('Do you have any hobbies ?', True, color_text)
    
    # Position the question text
    text_rect = q7.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the rectangle behind the text
    rect_width = 300
    rect_height = 50
    rect_x = text_rect.centerx - (rect_width // 2)
    rect_y = text_rect.bottom + 10

    
    # Draw the question text
    screen.blit(q7, text_rect.topleft)
    
    # Draw "Yes" and "No" buttons
    button_width = 100
    button_height = 40
    
    # Center the buttons below the text
    total_buttons_width = button_width * 2 + 20  # Add space between buttons
    buttons_x = text_rect.centerx - (total_buttons_width // 2)
    
    yes_button_rect = pygame.Rect(buttons_x, rect_y , button_width, button_height)
    no_button_rect = pygame.Rect(buttons_x + button_width + 20, rect_y , button_width, button_height)
    
    pygame.draw.rect(screen, color_rect, yes_button_rect)
    pygame.draw.rect(screen, color_rect, no_button_rect)
    
    yes_text = font_menu.render('Yes', True, color_text)
    no_text = font_menu.render('No', True, color_text)
    
    # Center the text inside the buttons
    screen.blit(yes_text, yes_button_rect.move((button_width - yes_text.get_width()) // 2, (button_height - yes_text.get_height()) // 2))
    screen.blit(no_text, no_button_rect.move((button_width - no_text.get_width()) // 2, (button_height - no_text.get_height()) // 2))

def page9():
    draw_background()  # Show the background
    q7 = font_menu.render('Still doing it right ??', True, color_text)
    
    # Position the question text
    text_rect = q7.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the question text
    screen.blit(q7, text_rect.topleft)
    
    # Draw "Yes", "I do not know", and "No" buttons
    button_texts = ['of course', 'Sometime', 'No']  # Swapped "No" and "I do not know"
    button_widths = []
    button_heights = []
    button_rects = []
    
    for text in button_texts:
        text_surf = font_menu.render(text, True, color_text)
        button_widths.append(text_surf.get_width() + 20)  # Adding padding
        button_heights.append(text_surf.get_height() + 10)  # Adding padding
    
    total_buttons_width = sum(button_widths) + 20 * (len(button_texts) - 1)  # Space between buttons
    buttons_x = text_rect.centerx - (total_buttons_width // 2)
    buttons_y = text_rect.bottom + 20  # Adjust this value to position buttons
    
    # Create button rectangles
    for i, (text, width, height) in enumerate(zip(button_texts, button_widths, button_heights)):
        rect = pygame.Rect(buttons_x, buttons_y, width, height)
        button_rects.append(rect)
        buttons_x += width + 20  # Move x position for next button

    # Draw rectangles and text
    for rect, text in zip(button_rects, button_texts):
        pygame.draw.rect(screen, color_rect, rect)
        text_surf = font_menu.render(text, True, color_text)
        text_rect = text_surf.get_rect(center=rect.center)
        screen.blit(text_surf, text_rect.topleft)

def page10():
    draw_background()  # Show the background
    # Render the texts
    q9 = font_menu.render('So how much do you want to trade?', True, color_text)
    q2 = font_menu.render('1 year = 8760 hours', True, color_text)

    # Position the first text
    text_rect_q9 = q9.get_rect(center=(screen_width // 2, (screen_height // 2) - 30))

    # Position the second text
    text_rect_q2 = q2.get_rect(center=(screen_width // 2, (screen_height // 2) + 10))
    
    # Draw a rectangle under the second text
    rect_width_q2 = text_rect_q2.width + 20  # Add padding to the width
    rect_height_q2 = text_rect_q2.height + 20  # Add padding to the height
    rect_x_q2 = text_rect_q2.centerx - (rect_width_q2 // 2)
    rect_y_q2 = text_rect_q2.bottom + 10  # Position the rectangle slightly below the text
    rect_q2 = pygame.Rect(rect_x_q2, rect_y_q2, rect_width_q2, rect_height_q2)
    
    pygame.draw.rect(screen, color_rect, rect_q2)
    
    # Draw the texts
    screen.blit(q9, text_rect_q9.topleft)
    screen.blit(q2, text_rect_q2.topleft)

def page11():   
    draw_background()  # Show the background
    q7 = font_menu.render('Are you ready to play ?', True, color_text)
    
    # Position the question text
    text_rect = q7.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the rectangle behind the text
    rect_width = 300
    rect_height = 50
    rect_x = text_rect.centerx - (rect_width // 2)
    rect_y = text_rect.bottom + 10

    
    # Draw the question text
    screen.blit(q7, text_rect.topleft)
    
    # Draw "Yes" and "No" buttons
    button_width = 100
    button_height = 40
    
    # Center the buttons below the text
    total_buttons_width = button_width * 2 + 20  # Add space between buttons
    buttons_x = text_rect.centerx - (total_buttons_width // 2)
    
    yes_button_rect = pygame.Rect(buttons_x, rect_y , button_width, button_height)
    no_button_rect = pygame.Rect(buttons_x + button_width + 20, rect_y , button_width, button_height)
    
    pygame.draw.rect(screen, color_rect, yes_button_rect)
    pygame.draw.rect(screen, color_rect, no_button_rect)
    
    yes_text = font_menu.render('Yes', True, color_text)
    no_text = font_menu.render('No', True, color_text)
    
    # Center the text inside the buttons
    screen.blit(yes_text, yes_button_rect.move((button_width - yes_text.get_width()) // 2, (button_height - yes_text.get_height()) // 2))
    screen.blit(no_text, no_button_rect.move((button_width - no_text.get_width()) // 2, (button_height - no_text.get_height()) // 2))

run = True
page_number = 1  # Track which page we are on

while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            page_number += 1  # Increment the page number on each click

        if event.type == pygame.QUIT:
            run = False

    # Display different content based on the current page number
    if page_number == 1:
        page1()  # Show page 1
    elif page_number == 2:
        page2()  # Show page 2
    elif page_number == 3:
        page3()  # Show page 3
    elif page_number == 4:
        page4()  # Show page 3
    elif page_number == 5:
        page5()  # Show page 3
    elif page_number == 6:
        page6()  # Show page 3
    elif page_number == 7:
        page7()  # Show page 3
    elif page_number == 8 :
        page8()
    elif page_number == 9 :
        page9()
    elif page_number == 10 :
        page10()
    elif page_number == 11 :
        page11()
    
    else:
        screen.fill((0, 0, 0))  # After page 3, keep the screen black

    pygame.display.flip()

pygame.quit()



