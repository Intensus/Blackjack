import random
import time
import os
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def draw_cards(hand, deck, n):
    for i in range(0, n):
        card = deck.pop()
        hand.append(card)


def count_hand(hand):
    total = 0
    aces: int = 0
    for card in hand:
        match card:
            case "A":
                if aces == 0:
                    total += 11
                    aces = 1
                else:
                    total += 1
            case "J":
                total += 10
            case "Q":
                total += 10
            case "K":
                total += 10
            case other:
                total += card
    return total


original_deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             ]
card_deck=shuffle_deck(original_deck)
clear_screen()
print(logo)
print("Welcome to the Little Personal casino!")
print("Here fun gets a little personal!")
print("")
new_round=True
while new_round:

    # If deck is low on cards, reshuffle.
    if len(card_deck)<10:
        print("Reshuffling cards...")
        time.sleep(2)
        card_deck=shuffle_deck(original_deck)

    # Draw 2 cars each, show cards.
    player_hand = []
    dealer_hand = []
    draw_cards(player_hand, card_deck, 2)
    draw_cards(dealer_hand, card_deck, 2)
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: [*, {dealer_hand[1]}]")
    winner = ""
    keep_dealing = True

    # Check if anyone has already won.

    # Ask if they want more cards.
    while keep_dealing:
        deal_new_card = ""
        while deal_new_card != "y" and deal_new_card != "n":
            deal_new_card = input("Deal a card? (y/n) ")
        if deal_new_card == "y":
            draw_cards(player_hand, card_deck, 1)
            print(f"Player's hand: {player_hand}")
            player_total = count_hand(player_hand)

            # Check if they have got 21 or lost.
            if player_total == 21:
                keep_dealing = False
            if player_total > 21:
                winner = "dealer"
                keep_dealing = False
        if deal_new_card == "n":
            keep_dealing = False

    print(f"Dealer's hand: {dealer_hand}")
    player_total = count_hand(player_hand)
    dealer_total = count_hand(dealer_hand)
    if winner != "dealer":
        while dealer_total < player_total and dealer_total < 22:
            draw_cards(dealer_hand, card_deck, 1)
            dealer_total = count_hand(dealer_hand)
            print(f"Dealer's hand: {dealer_hand}")
            time.sleep(2)
        if dealer_total < 22 and not dealer_total < player_total:
            winner="dealer"
        else:
            winner="player"

    # Declare winner
    print(f"You have {player_total}.")
    print(f"Dealer has {dealer_total}.")
    match winner:
        case "player":
            print("You win!")
        case "dealer":
            print("Dealer wins!")

    ask_new_round=""
    while ask_new_round != "y" and ask_new_round != "n":
        ask_new_round=input("Play another round? (y/n) ").lower()
    if ask_new_round=="n":
        new_round=False
        print("Ok, see you soon!")
    else:
        clear_screen()

