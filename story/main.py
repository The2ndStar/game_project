import pygame
import sys
import pygame_gui
import json
import os
import time
sys.path.append(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project')
from menu.gameselect import gameselect




def Story(screen) :
    from pygame.locals import QUIT
    pygame.init()
    screen_width = 800
    screen_height = 500

    color_text = (255, 255, 255)
    color_rect = (188,159,124)

    page_number = 1

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("แดนอบาย888")

    pygame.mixer.music.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\sound\Bg_sound.mp3")
    pygame.mixer.music.play(-1)

    bg_story1 = pygame.image.load(r"C:\Users\Woranat\OneDrive\Desktop\algro\game_project\photo\4.png")
    font_menu = pygame.font.Font(r'C:\Users\Woranat\OneDrive\Desktop\algro\game_project\FONT\BASKVILL.TTF', 30)

    def write_to_json(data, filename='user_data.json'):
        try:
        # Try to read existing data from the file
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
        # If file does not exist, initialize with an empty list
            existing_data = []
        except json.JSONDecodeError:
        # Handle case where file is empty or corrupt
            existing_data = []

    # Append new data to the existing data
        existing_data.append(data)

        try:
        # Write updated data back to the file
            with open(filename, 'w') as file:
                json.dump(existing_data, file, indent=4)
        except IOError as e:
        # Handle file writing errors
            print(f"Error writing to file: {e}")

    def draw_background():
        back_size = pygame.transform.scale(bg_story1, (screen_width, screen_height))
        screen.blit(back_size, (0, 0))

    def page1(screen):
        draw_background()
        welcome_text1 = font_menu.render('warmly welcome lost gambler', True, color_text)
        welcome_text2 = font_menu.render('We are waiting for you', True, color_text)
        screen.blit(welcome_text1, ((screen_width / 4) + 20, (screen_height / 3) + 15))
        screen.blit(welcome_text2, ((screen_width / 4) + 50, (screen_height / 2) + 15))

    def page2(screen):
        screen.fill((0, 0, 0))  # Clear the screen with black color
        textq1 = font_menu.render('You arrived', True, color_text)
        screen.blit(textq1, ((screen_width /2)-90, (screen_height /2)-10))

    def page3(screen):
        draw_background()  # Show the background
        Clock = pygame.time.Clock()
        Manager = pygame_gui.UIManager((screen_width, screen_height))

    # Render the question above the input box
        q1 = font_menu.render('Well, who are you then?', True, color_text)
        text_rect = q1.get_rect(center=(screen_width // 2, (screen_height // 2) - 75))  # Positioned above input box

    # Define the input box dimensions
        rect_x, rect_y = screen_width // 2 - 150, screen_height // 2 - 20
        rect_width, rect_height = 300, 50

    # Create a text input line, with no background (transparent)
        TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((rect_x, rect_y), (rect_width, rect_height)),
            manager=Manager
        )

        user_input = ""  # Store user input
        input_finished = False  # Flag to check if input is done
        running = True
        timer_started = 0  # Timer for flipping page after input

        while running:
            UI_refresh = Clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                Manager.process_events(event)

            # Handle input submission
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == TEXT_INPUT:
                    user_input = event.text  # Capture the input text
                    input_finished = True  # Set flag when input is done
                    timer_started = pygame.time.get_ticks()  # Start timer to flip the page

                    write_to_json({"user_Name": user_input})
        
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
                    page4(screen)  # Call the next page function
                    return  # Exit the function after transitioning

            pygame.display.update()

    def page4(screen):
        draw_background()  # Show the background
        Clock = pygame.time.Clock()
        Manager = pygame_gui.UIManager((screen_width, screen_height))
    
        q2 = font_menu.render('How long did you Advent?', True, color_text)
        text_rect = q2.get_rect(center=(screen_width // 2, (screen_height // 2-40)))
        rect_x, rect_y = screen_width // 2 - 150, screen_height // 2
        rect_width, rect_height = 300, 50

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

                    write_to_json({"age": user_input})
        
            Manager.update(UI_refresh)
            draw_background()  # Redraw the background for smooth UI update

        # Draw the question text
            screen.blit(q2, text_rect.topleft)

        # Draw the filled rectangle for the input box with 'color_rect'
            pygame.draw.rect(screen, color_rect, (rect_x, rect_y, rect_width, rect_height))  # Filled rectangle

        # Draw the text input field (no need for a separate rectangle border)
            Manager.draw_ui(screen)

        # If the input is finished, display the follow-up text
            if input_finished:
                textq2 = font_menu.render(f"That a long time huh?!", True, color_text)
                screen.blit(textq2, ((screen_width // 2) - 150, (screen_height // 2) + 70))  # Positioned below input

            # After showing the text, wait for 2 seconds then flip to page 4
                if pygame.time.get_ticks() - timer_started > 2000:  # 2 seconds delay
                    page5(screen)  # Call the next page function

            pygame.display.update()
        
    def page5(screen):
        draw_background()  # Show the background
        Clock = pygame.time.Clock()

        q3 = font_menu.render('Do you love your life?', True, color_text)
    
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
    
        yes_button_rect = pygame.Rect(buttons_x, rect_y, button_width, button_height)
        no_button_rect = pygame.Rect(buttons_x + button_width + 20, rect_y, button_width, button_height)
    
        pygame.draw.rect(screen, color_rect, yes_button_rect)
        pygame.draw.rect(screen, color_rect, no_button_rect)
    
        yes_text = font_menu.render('Yes', True, color_text)
        no_text = font_menu.render('No', True, color_text)
    
    # Center the text inside the buttons
        screen.blit(yes_text, yes_button_rect.move((button_width - yes_text.get_width()) // 2, (button_height - yes_text.get_height()) // 2))
        screen.blit(no_text, no_button_rect.move((button_width - no_text.get_width()) // 2, (button_height - no_text.get_height()) // 2))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if yes_button_rect.collidepoint(mouse_pos) or no_button_rect.collidepoint(mouse_pos) :
                        page6(screen) 

            pygame.display.update()
            Clock.tick(60)

    def page6(screen):
        draw_background()  # Show the background
        clock = pygame.time.Clock()

    # Render the main question and additional text
        q5 = font_menu.render('What about your loved one?', True, color_text)
        t1 = font_menu.render('Are they appreciate your life?', True, color_text)
    
    # Position the main question text
        text_rect_q5 = q5.get_rect(center=(screen_width // 2, (screen_height // 2)-30))
    # Position the additional text
        text_rect_t1 = t1.get_rect(center=(screen_width // 2, (screen_height // 2)+10))

    # Draw the main question text
        screen.blit(q5, text_rect_q5.topleft)
    # Draw the additional text
        screen.blit(t1, text_rect_t1.topleft)
    
    # Draw "Yes", "I do not know", and "No" buttons
        button_texts = ['of course', 'I do not know', 'No']
        button_widths = []
        button_heights = []
        button_rects = []
    
        for text in button_texts:
            text_surf = font_menu.render(text, True, color_text)
            button_widths.append(text_surf.get_width() + 20)  # Adding padding
            button_heights.append(text_surf.get_height() + 10)  # Adding padding
    
        total_buttons_width = sum(button_widths) + 20 * (len(button_texts) - 1)  # Space between buttons
        buttons_x = text_rect_q5.centerx - (total_buttons_width // 2)
        buttons_y = text_rect_q5.bottom + 60  # Adjust this value to position buttons
    
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
    
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mouse_pos):
                        # Debug: print the button clicked
                            print(f"Button clicked: {button_texts[i]}")
                        # Determine which button was clicked and save to JSON
                            choice = button_texts[i]
                            write_to_json({"careing": choice})
                            print("Data written to JSON")
                            page7(screen)  # Call the next page function
                            return  # Exit the function after transitioning to the next page

            pygame.display.update()
            clock.tick(60)

    def page7(screen):
        draw_background()  # Show the background
        clock = pygame.time.Clock()

    # Render the question text
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

    # Combine all button rectangles into one list
        button_rects = button_rects_row1 + button_rects_row2
        button_texts = button_texts_row1 + button_texts_row2  # Flatten button texts for easy access

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mouse_pos):
                        # Determine which button was clicked and save to JSON
                            choice = button_texts[i]
                            write_to_json({"most_important": choice})
                            print(f"Button clicked: {choice}")
                            print("Data written to JSON")
                            page8(screen)  # Call the next page function
                            return  # Exit the function after transitioning to the next page

            pygame.display.update()
            clock.tick(60)

    def page8(screen):
        draw_background()  # Show the background
        clock = pygame.time.Clock()
    
        q7 = font_menu.render('Do you have any hobbies?', True, color_text)
    
    # Position the question text
        text_rect = q7.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the question text
        screen.blit(q7, text_rect.topleft)
    
    # Draw "Yes" and "No" buttons
        button_width = 100
        button_height = 40
    
    # Center the buttons below the text
        total_buttons_width = button_width * 2 + 20  # Add space between buttons
        buttons_x = text_rect.centerx - (total_buttons_width // 2)
    
        yes_button_rect = pygame.Rect(buttons_x, text_rect.bottom + 10, button_width, button_height)
        no_button_rect = pygame.Rect(buttons_x + button_width + 20, text_rect.bottom + 10, button_width, button_height)
    
        pygame.draw.rect(screen, color_rect, yes_button_rect)
        pygame.draw.rect(screen, color_rect, no_button_rect)
    
        yes_text = font_menu.render('Yes', True, color_text)
        no_text = font_menu.render('No', True, color_text)
    
    # Center the text inside the buttons
        screen.blit(yes_text, yes_button_rect.move((button_width - yes_text.get_width()) // 2, (button_height - yes_text.get_height()) // 2))
        screen.blit(no_text, no_button_rect.move((button_width - no_text.get_width()) // 2, (button_height - no_text.get_height()) // 2))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if yes_button_rect.collidepoint(mouse_pos):
                    # Save choice and move to the next page
                        write_to_json({"hobbies": "Yes"})
                        page9(screen)  # Call the next page function
                        return  # Exit function after saving and transitioning
                
                    if no_button_rect.collidepoint(mouse_pos):
                    # Save choice and move to the next page
                        write_to_json({"hobbies": "No"})
                        page9(screen)  # Call the next page function
                        return  # Exit function after saving and transitioning

            pygame.display.update()
            clock.tick(60)

    def page9(screen):
        draw_background()  # Show the background
        clock = pygame.time.Clock()
    
        q7 = font_menu.render('Still doing it right ??', True, color_text)
    
    # Position the question text
        text_rect = q7.get_rect(center=(screen_width // 2, (screen_height // 2) - 15))
    
    # Draw the question text
        screen.blit(q7, text_rect.topleft)
    
    # Draw "Yes", "I do not know", and "No" buttons
        button_texts = ['of course', 'Sometime', 'No']
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
    
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mouse_pos):
                        # Determine which button was clicked and save to JSON
                            choice = button_texts[i]
                            write_to_json({"doing_it_right": choice})
                            page10(screen)  # Call the next page function
                            return  # Exit function after saving and transitioning

            pygame.display.update()
            clock.tick(60)

    def page10(screen):
        draw_background()  # Show the background
        clock = pygame.time.Clock()
        Manager = pygame_gui.UIManager((screen_width, screen_height))

    # Render the texts
        q9 = font_menu.render('So how much do you want to trade?', True, color_text)
        q2 = font_menu.render('1 year = 8760 hours', True, color_text)

    # Position the texts
        text_rect_q9 = q9.get_rect(center=(screen_width // 2, (screen_height // 2) - 40))
        text_rect_q2 = q2.get_rect(center=(screen_width // 2, (screen_height // 2) + 10 ))

    # Draw the question text
        screen.blit(q9, text_rect_q9.topleft)

    # Create a text input line
        rect_x, rect_y = screen_width // 2 - 150, screen_height // 2 + 30
        rect_width, rect_height = 300, 50

        TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((rect_x, rect_y), (rect_width, rect_height)),
            manager=Manager
        )

        user_input = ""  # Store user input
        input_finished = False  # Flag to check if input is done
        show_error_message = False  # Flag to determine if the error message is shown
        valid_input_received = False  # Flag to indicate if valid input was received
        running = True
        timer_started = None  # Timer for displaying messages

        while running:
            UI_refresh = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                Manager.process_events(event)

            # Handle input submission
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == TEXT_INPUT:
                    user_input = event.text  # Capture the input text
                    try:
                        trade_hours = int(user_input)  # Convert input to int
                        if trade_hours < 95:
                            valid_input_received = True
                            total_hours = trade_hours * 8760
                            display_message = font_menu.render(f"You get {total_hours} hours!", True, color_text)
                            input_finished = True
                            timer_started = pygame.time.get_ticks()  # Start timer to flip the page
                            show_error_message = False
                        
                        # Save the user input to JSON
                            write_to_json({"trade_hours": trade_hours})
                        else:
                            display_message = font_menu.render("You don't have that much time!", True, color_text)
                            input_finished = True
                            timer_started = pygame.time.get_ticks()  # Start timer to show message
                            show_error_message = True
                    except ValueError:
                        display_message = font_menu.render("Invalid input. Please enter a number.", True, color_text)
                        input_finished = True
                        timer_started = pygame.time.get_ticks()  # Start timer to show message
                        show_error_message = True

            Manager.update(UI_refresh)
            draw_background()  # Redraw the background for smooth UI update

        # Draw the texts and rectangle
            screen.blit(q9, text_rect_q9.topleft)
            screen.blit(q2, text_rect_q2.topleft)

        # Draw the text input field
            pygame.draw.rect(screen, color_rect, (rect_x, rect_y, rect_width, rect_height))  # Filled rectangle
            Manager.draw_ui(screen)

        # If the input is finished
            if input_finished:
            # Draw the follow-up message
                screen.blit(display_message, ((screen_width // 2) - display_message.get_width() // 2, (screen_height // 2) + 85))  # Positioned below input

            # If showing an error message
                if show_error_message and pygame.time.get_ticks() - timer_started > 3000:  # 3 seconds delay for error message
                    input_finished = False
                    show_error_message = False
                    TEXT_INPUT.clear()  # Clear the previous input
                    user_input = ""  # Reset user input
                elif valid_input_received and pygame.time.get_ticks() - timer_started > 2000:  # 2 seconds delay for valid input
                    page11(screen)  # Call the next page function

            pygame.display.update()

    def page11(screen):
        draw_background()  # Show the background
        clock = pygame.time.Clock()
    
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
        


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if yes_button_rect.collidepoint(mouse_pos):
                        write_to_json({"ready_to_play": "Yes"})
                        gameselect(screen)  # Clear screen or proceed as needed
                        pygame.display.update()
                    # Proceed to the next page or action
                    elif no_button_rect.collidepoint(mouse_pos):
                        write_to_json({"ready_to_play": "No"})
                        gameselect(screen)  # Clear screen or proceed as needed
                        pygame.display.update()
                    # Proceed to the next page or action

            pygame.display.update()
            clock.tick(60)

    
    page_number = 1
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exit the loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                page_number += 1  # Flip to the next page on click

        draw_background()

        # Show different content based on the current page number
        if page_number == 1:
            page1(screen)
        elif page_number == 2:
            page2(screen)
        elif page_number == 3:
            page3(screen)
        elif page_number == 4:
            page4(screen)
        elif page_number == 5:
            page5(screen)
        elif page_number == 6:
            page6(screen)
        elif page_number == 7:
            page7(screen)
        elif page_number == 8:
            page8(screen)
        elif page_number == 9:
            page9(screen)
        elif page_number == 10:
            page10(screen)
        

        pygame.display.flip()  # Update the display

    return True  # Signal that `Story` has finished successfully
    
        




