"""
file: blackjack.py
language: python 3
author: Aakash Jaideva
purpose: A simple game of Blackjack
"""


import random


def deal_card():
    """
    Function to randomly select a card from the deck.
    Cards can have values 1 to 11 (inclusive), with face cards having a value of 10.
    """
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(cards):
    """
    Function to calculate the total score of a hand of cards.
    Handles the special case of an Ace being 1 or 11 based on the overall score.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Use Ace as 1 if using it as 11 would result in a bust.
    return sum(cards)


def compare(users_score, computers_score):
    """
    Function to compare the final scores and determine the winner or if it's a draw.
    """
    if users_score == computers_score:
        return "Draw"
    elif computers_score == 0:
        return "Lose. Opponent has blackjack"
    elif users_score == 0:
        return "Win with Blackjack"
    elif users_score > 21:
        return "You went over 21. You Lose"
    elif computers_score > 21:
        return "Opponent went over 21. You Win!"
    elif users_score > computers_score:
        return "You Win!"
    elif computers_score > users_score:
        return "You lose"


# Initialize player and computer hands
user_cards = []
computer_cards = []

# Deal two cards to each player
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Flag to track whether the game is over
is_game_over = False

# Main game loop
while not is_game_over:
    # Calculate scores for both player and computer
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Display current status
    print(f"Your cards: {user_cards}, current score: {user_score} ")
    print(f"Computer's first card: {computer_cards[0]}")

    # Check if the game should end
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        # Ask the user whether to get another card or pass
        user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_deal == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            # Check if the user busts
            if user_score > 21:
                is_game_over = True
                print(compare(user_score, computer_score))
        else:
            is_game_over = True

    # Computer's turn: Draw cards until the score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

# Display final hands and determine the winner
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
