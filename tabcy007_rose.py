import random
import dice

#
# File: tabcy007_converter.py
# Author: Chowdhury Nabila Tabassum
# Email Id: tabcy007@mymail.unisa.edu.au
# Description: Assignment 1 – menu driven program called tabcy007_rose.py that program allows the user to repeatedly guess the answer to the puzzle until the user chooses to stop guessing/playing. Once the user chooses to stop guessing, the program will report the user’s and game play statistics to the screen.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

print("File : tabcy007_converter.py")
print("Author : Chowdhury Nabila Tabassum")
print("Stud ID : 110405435")
print("Email ID : tabcy007@mymail.unisa.edu.au")
print("This is my own work as defined by the University's Academic Misconduct Policy.")

# Variable definitions
correct = 0  # Number of correct guesses
incorrect = 0  # Number of incorrect guesses
consecutive_incorrect = 0  # Number of consecutive incorrect guesses
consecutive_correct = 0  # Number of consecutive correct guesses
games_played = 0  # Number of games played
face_counts = [0, 0, 0, 0, 0, 0]  # Dice face counts

# Print the game title and instructions
print("\n\nPetals Around the Rose")
print("----------------------")
print("\nThe name of the game is 'Petals Around the Rose'. The name of the game is important. The computer will roll five dice and ask you to guess the score for the roll. The score will always be zero or an even number. Your mission, should you choose to accept it, is to work out how the computer calculates the score. If you succeed in working out the secret and guess correctly three times in a row, you become a Potentate of the Rose.")

# Ask the user if they want to play the game
play_again = input(
    '\nWould you like to play Petals Around the Rose? [y/n]? ')

# Counter to keep track of the number of times the game has been played
play_count = 0

# Check if the user entered a valid input
valid_input = False
while not valid_input:  # While the user has not entered a valid input
    if play_again == 'y':  # If the user wants to play the game
        valid_input = True
    elif play_again == 'n':  # If the user does not want to play the game
        valid_input = True
    else:  # If the user entered an invalid input
        play_again = input(
            "Please enter either 'y' or 'n' to play the game: ")

# If the user does not want to play the game, print a message
if (play_count == 0 and play_again == 'n'):
    print("\nNo worries... another time perhaps... :)")

# Keep playing the game as long as the user wants to
while play_again == 'y':

    play_count += 1  # Increment the number of times the game has been played

    dice_face = [random.randint(1, 6) for _ in range(5)]  # Roll the dice

    dice.display_dice(dice_face[0], dice_face[1],
                      dice_face[2], dice_face[3], dice_face[4])  # Display the dice

    # Calculate the score
    score = 0  # Initialise the score to zero
    for i in dice_face:  # For each dice face
        if i == 3:  # If the dice face is 3
            score += 2  # Add 2 to the score
        elif i == 5:  # If the dice face is 5
            score += 4  # Add 4 to the score

    # Ask the user to guess the score
    guess = int(input("\nPlease enter your guess for the roll: "))

    # Check if the user's guess is correct
    if guess == score:
        print("\nWell done! You guessed it!")
        correct += 1  # Increment the number of correct guesses
        consecutive_correct += 1  # Increment the number of consecutive correct guesses
        if consecutive_correct == 3:  # If the user has guessed correctly three times in a row
            print("\n\nCongratulations! You have worked out the secret!")
            print("Make sure you don't tell anyone!")
            consecutive_correct = 0  # Reset the number of consecutive correct guesses

    elif guess % 2 != 0:  # If the user's guess is not an even number
        print(
            f"\nNo sorry, it's {score} not {guess}. The score is always even.")
        incorrect += 1  # Increment the number of incorrect guesses
        consecutive_incorrect += 1  # Increment the number of consecutive incorrect guesses
        if consecutive_incorrect == 3:  # If the user has guessed incorrectly three times in a row
            print(
                "\nHint: The name of the game is important... Petals Around the Rose.")
            consecutive_incorrect = 0  # Reset the number of consecutive incorrect guesses

    else:  # If the user's guess is incorrect
        print(f"\nNo sorry, it's {score} not {guess}.")
        incorrect += 1  # Increment the number of incorrect guesses
        consecutive_incorrect += 1  # Increment the number of consecutive incorrect guesses
        if consecutive_incorrect == 3:  # If the user has guessed incorrectly three times in a row
            print(
                "\nHint: The name of the game is important... Petals Around the Rose.")
            consecutive_incorrect = 0  # Reset the number of consecutive incorrect guesses

    # Update the dice face counts
    for d in dice_face:  # For each dice face
        face_counts[d-1] += 1  # Increment the dice face count

    # Ask the user if they want to play again
    games_played += 1  # Increment the number of games played
    # Ask the user if they want to play again
    play_again = input("\n\nRoll dice again [y|n]? ")

    # Check if the user entered a valid input
    valid_input = False

    # While the user has not entered a valid input
    while not valid_input:
        if play_again == 'y':
            valid_input = True
        elif play_again == 'n':
            valid_input = True
        else:
            play_again = input(
                "Please enter either 'y' or 'n'. \n\nRoll dice again [y|n]? ")

# Print the game summary
if games_played > 0:  # If the user has played at least one game
    print("\nGame Summary")
    print("============")
    print(f"\nYou played {games_played} games:")
    print(f" |--> Number of correct guesses:\t{correct}")
    print(f" |--> Number of incorrect guesses:\t{incorrect}")
    print("\n\nDice Roll Stats:")
    print("\nFace Frequency")

    # Print the dice face counts
    for i in range(6):  # For each dice face
        print(f"\t{i+1} {face_counts[i]*'*'}")  # Print the dice face count

# If the user has not played the game, print a message
if (play_count != 0 and play_again == 'n'):
    print("\nThanks for playing!")
