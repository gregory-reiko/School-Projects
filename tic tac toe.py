import random
from tkinter import *

window = Tk()
window.title("Tic Tac Toe")

who_makes_turn = random.randint(0, 1)
what_to_retry = 0

# Translates the 0 or 1 in who_makes_turn into a string of "X" or "O".
def X_or_O():
    if who_makes_turn == 0:
        return "X"
    else:
        return "O"

# Currently used so that the retry button in victory_conditions() knows what gamemode to retry when you press it.
def gamemode():
    if what_to_retry == 0:
        return multiplayer
    elif what_to_retry == 1:
        return easy_computer
    elif what_to_retry == 2:
        return medium_computer
    else:
        return hard_computer

# Checks if the victory or tie conditions have been met, if so, then replaces everything on the screen with the end of the game screen and returns True.
def victory_conditions(play_area_in_victory_conditions, X_or_O_in_victory_conditions, buttons_frame_in_victory_conditions):
    global who_makes_turn
    
    if ((play_area_in_victory_conditions[0]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[1]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[2]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[3]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[4]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[5]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[6]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[7]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[8]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[0]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[3]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[6]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[1]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[4]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[7]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[2]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[5]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[8]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[0]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[4]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[8]["text"] == X_or_O_in_victory_conditions) or
    (play_area_in_victory_conditions[2]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[4]["text"] == X_or_O_in_victory_conditions and play_area_in_victory_conditions[6]["text"] == X_or_O_in_victory_conditions)):
        who_makes_turn = random.randint(0, 1)
        
        buttons_frame_in_victory_conditions.destroy()
        
        victory_conditions_frame_win = Frame(window)
        victory_conditions_frame_win.grid()
        
        victory_conditions_label_win = Label(victory_conditions_frame_win, text = X_or_O_in_victory_conditions + " " + "has won the game!", height = 5, width = 40)
        victory_conditions_label_win.grid(column = 0, row = 0)
        
        retry_button_in_victory_conditions_win = Button(victory_conditions_frame_win, text = "RETRY", height = 5, width = 40, command = lambda:buttons(victory_conditions_frame_win, gamemode()))
        retry_button_in_victory_conditions_win.grid(column = 0, row = 1)
        
        back_to_menu_button_in_victory_conditions_win = Button(victory_conditions_frame_win, text = "BACK TO MENU", height = 5, width = 40, command = lambda:menu(victory_conditions_frame_win))
        back_to_menu_button_in_victory_conditions_win.grid(column = 0, row = 2)
        
        quit_button_in_victory_conditions_win = Button(victory_conditions_frame_win, text = "QUIT", height = 5, width = 40, command = lambda:quit(window))
        quit_button_in_victory_conditions_win.grid(column = 0, row = 3)
        
        return True
    elif (play_area_in_victory_conditions[0]["text"] != " " and play_area_in_victory_conditions[1]["text"] != " " and play_area_in_victory_conditions[2]["text"] != " " and
    play_area_in_victory_conditions[3]["text"] != " " and play_area_in_victory_conditions[4]["text"] != " " and play_area_in_victory_conditions[5]["text"] != " " and
    play_area_in_victory_conditions[6]["text"] != " " and play_area_in_victory_conditions[7]["text"] != " " and play_area_in_victory_conditions[8]["text"] != " "):
        who_makes_turn = random.randint(0, 1)
        
        buttons_frame_in_victory_conditions.destroy()
        
        victory_conditions_frame_tie = Frame(window)
        victory_conditions_frame_tie.grid()
        
        victory_conditions_label_tie = Label(victory_conditions_frame_tie, text = "It's a tie!", height = 5, width = 40)
        victory_conditions_label_tie.grid(column = 0, row = 0)
        
        retry_button_in_victory_conditions_tie = Button(victory_conditions_frame_tie, text = "RETRY", height = 5, width = 40, command = lambda:buttons(victory_conditions_frame_tie, gamemode()))
        retry_button_in_victory_conditions_tie.grid(column = 0, row = 1)
        
        back_to_menu_button_in_victory_conditions_tie = Button(victory_conditions_frame_tie, text = "BACK TO MENU", height = 5, width = 40, command = lambda:menu(victory_conditions_frame_tie))
        back_to_menu_button_in_victory_conditions_tie.grid(column = 0, row = 2)
        
        quit_button_in_victory_conditions_tie = Button(victory_conditions_frame_tie, text = "QUIT", height = 5, width = 40, command = lambda:quit(window))
        quit_button_in_victory_conditions_tie.grid(column = 0, row = 3)
        
        return True

# Checks if the pressed button is empty, communicates with victory_conditions() and switches turns for the multiplayer gamemode.
def multiplayer(pressed_button_in_multiplayer, play_area_in_multiplayer, buttons_frame_in_multiplayer):
    global who_makes_turn
    global what_to_retry
    
    what_to_retry = 0
    
    if pressed_button_in_multiplayer["text"] == " ":
        pressed_button_in_multiplayer["text"] = X_or_O()
        
        victory_conditions(play_area_in_multiplayer, X_or_O(), buttons_frame_in_multiplayer)
        
        if who_makes_turn == 0:
            who_makes_turn = 1
        else:
            who_makes_turn = 0

# Checks if the pressed button is empty, communicates with victory_conditions(), chooses a random button to make a move in and switches turns for the easy computer gamemode.
def easy_computer(pressed_button_in_easy_computer, play_area_in_easy_computer, buttons_frame_in_easy_computer):
    global who_makes_turn
    global what_to_retry
    
    what_to_retry = 1
    
    if pressed_button_in_easy_computer["text"] == " ":
        pressed_button_in_easy_computer["text"] = X_or_O()
        
        if victory_conditions(play_area_in_easy_computer, X_or_O(), buttons_frame_in_easy_computer) != True:
            
            while True:
                easy_computer_choice = random.randint(0, 8)
                
                if play_area_in_easy_computer[easy_computer_choice]["text"] == " " and who_makes_turn == 0:
                    play_area_in_easy_computer[easy_computer_choice]["text"] = "O"
                    
                    victory_conditions(play_area_in_easy_computer, "O", buttons_frame_in_easy_computer)
                    
                    break
                elif play_area_in_easy_computer[easy_computer_choice]["text"] == " " and who_makes_turn == 1:
                    play_area_in_easy_computer[easy_computer_choice]["text"] = "X"
                    
                    victory_conditions(play_area_in_easy_computer, "X", buttons_frame_in_easy_computer)
                    
                    break

# Removes last frame and creates the computer difficulty buttons which, when pressed, connect to buttons().
def computer_difficulty(last_frame_in_computer_difficulty):
    last_frame_in_computer_difficulty.destroy()
    
    computer_difficulty_selection_frame = Frame(window)
    computer_difficulty_selection_frame.grid()
    
    easy_button = Button(computer_difficulty_selection_frame, text = "EASY", height = 5, width = 40, command = lambda:buttons(computer_difficulty_selection_frame, easy_computer))
    easy_button.grid(column = 0, row = 0)
    
    medium_button = Button(computer_difficulty_selection_frame, text = "MEDIUM", height = 5, width = 40, command = lambda:quit(window))
    medium_button.grid(column = 0, row = 1)
    
    hard_button = Button(computer_difficulty_selection_frame, text = "HARD", height = 5, width = 40, command = lambda:quit(window))
    hard_button.grid(column = 0, row = 2)

# Removes last frame and creates the multiplayer, computer and back to menu buttons. Multiplayer connects to buttons(), computer connects to computer_difficulty() and back to menu connects to menu().
def multiplayer_or_computer(last_frame_in_multiplayer_or_computer):
    last_frame_in_multiplayer_or_computer.destroy()
    
    multiplayer_or_computer_selection_frame = Frame(window)
    multiplayer_or_computer_selection_frame.grid()
    
    multiplayer_button = Button(multiplayer_or_computer_selection_frame, text = "MULTIPLAYER", height = 5, width = 40, command = lambda:buttons(multiplayer_or_computer_selection_frame, multiplayer))
    multiplayer_button.grid(column = 0, row = 0)
    
    computer_button = Button(multiplayer_or_computer_selection_frame, text = "COMPUTER", height = 5, width = 40, command = lambda:computer_difficulty(multiplayer_or_computer_selection_frame))
    computer_button.grid(column = 0, row = 1)
    
    back_to_menu_button_in_multiplayer_or_computer = Button(multiplayer_or_computer_selection_frame, text = "BACK TO MENU", height = 5, width = 40, command = lambda:menu(multiplayer_or_computer_selection_frame))
    back_to_menu_button_in_multiplayer_or_computer.grid(column = 0, row = 2)

# Closes the program when connected to.
def quit(window_in_quit):
    window_in_quit.destroy()

# Removes last frame and creates the play and quit buttons. Play connects to multiplayer_or_computer() and quit connects to quit().
def menu(last_frame_in_menu):
    last_frame_in_menu.destroy()
    
    menu_frame = Frame(window)
    menu_frame.grid()
    
    play_button = Button(menu_frame, text = "PLAY", height = 5, width = 40, command = lambda:multiplayer_or_computer(menu_frame))
    play_button.grid(column = 0, row = 0)
    
    quit_button_in_menu = Button(menu_frame, text = "QUIT", height = 5, width = 40, command = lambda:quit(window))
    quit_button_in_menu.grid(column = 0, row = 1)

# Removes last frame and creates the 9 buttons used to play the game. When a button is pressed it connects to one of the gamemode functions depending on what gamemode you chose.
def buttons(last_frame_in_buttons, chosen_gamemode):
    global who_makes_turn
    
    last_frame_in_buttons.destroy()
    
    buttons_frame = Frame(window)
    buttons_frame.grid()
    
    button1 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[0], play_area, buttons_frame))
    button1.grid(column = 0, row = 0)
    
    button2 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[1], play_area, buttons_frame))
    button2.grid(column = 1, row = 0)
    
    button3 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[2], play_area, buttons_frame))
    button3.grid(column = 2, row = 0)
    
    button4 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[3], play_area, buttons_frame))
    button4.grid(column = 0, row = 1)
    
    button5 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[4], play_area, buttons_frame))
    button5.grid(column = 1, row = 1)
    
    button6 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[5], play_area, buttons_frame))
    button6.grid(column = 2, row = 1)
    
    button7 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[6], play_area, buttons_frame))
    button7.grid(column = 0, row = 2)
    
    button8 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[7], play_area, buttons_frame))
    button8.grid(column = 1, row = 2)
    
    button9 = Button(buttons_frame, text = " ", font = "Times 30 bold", height = 4, width = 8, command = lambda:chosen_gamemode(play_area[8], play_area, buttons_frame))
    button9.grid(column = 2, row = 2)
    
    play_area = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    
    user_or_computer = random.randint(0, 1)
    easy_computer_what_button = random.randint(0, 8)
    
    if chosen_gamemode == easy_computer and user_or_computer == 1 and who_makes_turn == 0:
        play_area[easy_computer_what_button]["text"] = X_or_O()
        who_makes_turn = 1
    elif chosen_gamemode == easy_computer and user_or_computer == 1 and who_makes_turn == 1:
        play_area[easy_computer_what_button]["text"] = X_or_O()
        who_makes_turn = 0

start_frame = Frame(window)
start_frame.grid()

start_button = Button(start_frame, text = "START", height = 5, width = 40, command = lambda:menu(start_frame))
start_button.grid(column = 0, row = 0)

window.mainloop()
