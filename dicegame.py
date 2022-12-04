#!/usr/local/anaconda3/bin/python3.9

# Write a simple dice game using PyGame in Python.
# Display two six-sided dice side by side.
# Below the dice, an up-arrow button and a down-arrow button are displayed.
# If the user guesses the next dice roll will be greater than the current roll, the user presses the up-arrow button (and the down-arrow button is depressed, if pressed).
# If the user guesses the next dice roll will be below the current roll, the user presses the down-arrow button (and the up-arrow button is depressed, if pressed).
# When the user touches or clicks the dice, both dice are set to randomly chosen values.  The new value is compared with the previous value.
# If the comparison matches the user's guess, then display a "you won" message and play the sound of a joyous bell ringing.
# If the comparison does not match the user's guess, then display a "you lost" message and play the sound of a sad bell ringing.
# The user can then guess again.
#
# The dice images are from http://www.clker.com/clipart-dice-1.html
# The bell sounds are from http://www.freesound.org/people/juskiddink/sounds/146722/
#
# Written by Eric P. Scott for CSE 20211, Lab 10, March 2016

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DICE_WIDTH = 222
DICE_HEIGHT = 222
DICE_SPACING = 50
BUTTON_WIDTH = 64
BUTTON_HEIGHT = 64
BUTTON_SPACING = 64


# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Dice Game")

# Load the dice images
dice1 = pygame.image.load("dice1.png").convert()
dice2 = pygame.image.load("dice2.png").convert()
dice3 = pygame.image.load("dice3.png").convert()
dice4 = pygame.image.load("dice4.png").convert()
dice5 = pygame.image.load("dice5.png").convert()
dice6 = pygame.image.load("dice6.png").convert()

# Load the button images
up_button = pygame.image.load("up_button.png").convert()
down_button = pygame.image.load("down_button.png").convert()

# Load the bell sounds
bell_sound = pygame.mixer.Sound("bell.wav")
sad_bell_sound = pygame.mixer.Sound("sad_bell.wav")

# Set the current dice values
dice1_value = 1
dice2_value = 1

# Set the current button states
up_button_pressed = False
down_button_pressed = False

# Set the current game state
game_state = "playing"

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # --- Game logic should go here

        # --- Drawing code should go here

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # Draw the dice
        if dice1_value == 1:
            screen.blit(dice1, [SCREEN_WIDTH / 2 - DICE_WIDTH - DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice1_value == 2:
            screen.blit(dice2, [SCREEN_WIDTH / 2 - DICE_WIDTH - DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice1_value == 3:
            screen.blit(dice3, [SCREEN_WIDTH / 2 - DICE_WIDTH - DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice1_value == 4:
            screen.blit(dice4, [SCREEN_WIDTH / 2 - DICE_WIDTH - DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice1_value == 5:
            screen.blit(dice5, [SCREEN_WIDTH / 2 - DICE_WIDTH - DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice1_value == 6:
            screen.blit(dice6, [SCREEN_WIDTH / 2 - DICE_WIDTH - DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])

        if dice2_value == 1:
            screen.blit(dice1, [SCREEN_WIDTH / 2 + DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice2_value == 2:
            screen.blit(dice2, [SCREEN_WIDTH / 2 + DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice2_value == 3:
            screen.blit(dice3, [SCREEN_WIDTH / 2 + DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice2_value == 4:
            screen.blit(dice4, [SCREEN_WIDTH / 2 + DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice2_value == 5:
            screen.blit(dice5, [SCREEN_WIDTH / 2 + DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])
        elif dice2_value == 6:
            screen.blit(dice6, [SCREEN_WIDTH / 2 + DICE_SPACING / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2])

        # Draw the buttons
        if up_button_pressed:
            screen.blit(up_button, [SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + BUTTON_SPACING / 2])
        else:
            screen.blit(up_button, [SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 - BUTTON_HEIGHT - BUTTON_SPACING / 2])

        if down_button_pressed:
            screen.blit(down_button, [SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + BUTTON_HEIGHT + BUTTON_SPACING / 2])
        else:
            screen.blit(down_button, [SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + BUTTON_SPACING / 2])

        # Draw the game state
        if game_state == "playing":
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Guess the next roll!", True, BLACK)
            screen.blit(text, [SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2 - text.get_height()])
        elif game_state == "won":
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("You won!", True, GREEN)
            screen.blit(text, [SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2 - text.get_height()])
        elif game_state == "lost":
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("You lost!", True, RED)
            screen.blit(text, [SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - DICE_HEIGHT / 2 - text.get_height()])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
