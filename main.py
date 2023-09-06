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
    aces = 0
    for card in hand:
        match card:
            case "A":
                # Count the aces, but do not add them to total yet, due to their ambiguity.
                aces += 1
            case "J":
                total += 10
            case "Q":
                total += 10
            case "K":
                total += 10
            case other:
                total += card
    if aces>0:
        sum_aces = aces - 1 + 11
        if sum_aces+total > 21:
            sum_aces = aces * 1
        total += sum_aces
    return total


original_deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
             ]

card_deck = shuffle_deck(original_deck).copy()
money = 100
clear_screen()
print(logo)
print("Welcome to the Little Personal casino!")
print("Here fun gets a little personal!")
print("")
new_round = True
while new_round:

    # If deck is low on cards, reshuffle.
    if len(card_deck)<12:
        print("Reshuffling cards...")
        time.sleep(2)
        card_deck = shuffle_deck(original_deck).copy()

    # Place bet
    bet=0
    while bet<1 or bet>money:
        correct_bet = False
        while not correct_bet:
            print(f"You have ${money}.")
            bet=input("Place your bet: $")
            if bet.isnumeric():
                correct_bet = True
                bet=int(bet)

    # Draw 2 cars each, show cards.
    winner = ""
    player_hand = []
    dealer_hand = []
    draw_cards(player_hand, card_deck, 2)
    draw_cards(dealer_hand, card_deck, 2)
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: [*, {dealer_hand[1]}]")
    keep_dealing = True

    # Check if anyone has already won.
    dealer_total=count_hand(dealer_hand)
    player_total=count_hand(player_hand)
    if dealer_total==21 or player_total==21:
        keep_dealing=False

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
        while dealer_total < 17 and dealer_total < 22:
            draw_cards(dealer_hand, card_deck, 1)
            dealer_total = count_hand(dealer_hand)
            print(f"Dealer's hand: {dealer_hand}")
            time.sleep(2)
        if dealer_total < 22 and dealer_total > player_total:
            winner="dealer"
        elif dealer_total == player_total:
            winner="draw"
        else:
            winner="player"

    # Declare winner
    print(f"You have {player_total}.")
    print(f"Dealer has {dealer_total}.")
    match winner:
        case "player":
            print("You win!")
            money+=bet
        case "dealer":
            print("Dealer wins!")
            money-=bet
        case "draw":
            print("It's a draw!")

    if money==0:
        print("You have lost all your money... Try again another time!")
        new_round=False
    else:
        ask_new_round=""
        while ask_new_round != "y" and ask_new_round != "n":
            ask_new_round=input("Play another round? (y/n) ").lower()
        if ask_new_round=="n":
            new_round=False
            print(f"You're leaving with ${money}. See you soon!")
        else:
            clear_screen()

