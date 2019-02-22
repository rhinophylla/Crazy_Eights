
import itertools
import random


def player_card_display(player, player_hands):
    """Print player's cards in a numbered list on the screen."""
    print("{0}, your hand contains the following cards: ".format(player))
    for index, element in enumerate(player_hands[player]):
        print("{0}: {1} of {2}".format(str(index+1), element[0], element[1]))

def crazy_eight_player(top_card):
    """Take player input on suit of a crazy eight and return card tuple."""
    suit = input("What suit do you want your crazy eight to be? ")
    try:
        if suit[0].lower() == 'd':
            top_card = (8, "Diamonds")
        elif suit[0].lower() == 'h':
            top_card = (8, "Hearts")
        elif suit[0].lower() == 'c':
            top_card = (8, "Clubs")
        elif suit[0].lower() == 's':
            top_card = (8, "Spades")
        else:
            raise ValueError
    except:
        print("You didn't enter diamonds, hearts, clubs, or spades.  Please try again.")
        return crazy_eight_player(top_card)
    return top_card

def is_play_valid(player, player_hands, top_card):
    """Take player input on next action and return integer."""
    try:
        card_index = input(
            "Enter the number of the card you want to play or enter 0 to draw a card. ")
        if card_index not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
            print("You must enter a number.")
            raise ValueError
        if int(card_index) < -1 or int(card_index) > len(player_hands[player]):
            print("The number you entered does not correspond to a card in your hand.")
            raise ValueError
        card_index_adj = int(card_index) - 1
        if player_hands[player][card_index_adj][0] == 8:
            return card_index_adj
        if card_index_adj == -1:
            return card_index_adj
        if top_card[0] == 8 and player_hands[player][card_index_adj][1] != top_card[1]:
            print("The suit of your card does not match the declared suit of the crazy eight!")
            raise ValueError
        if player_hands[player][card_index_adj][0] != top_card[0] and player_hands[player][card_index_adj][1] != top_card[1]:
            print("The number or suit of your card does not match the number or suit of the top card.")
            raise ValueError
        return card_index_adj
    except:
        print("Invalid entry or card play.  Please try again.")
        return is_play_valid(player, player_hands, top_card)


def player_turn(player, player_hands, deck, card):
    """Orchestrate steps of the player's turn and return new top card tuple.

    Arguments:
    player -- inputed name of player
    player_hands -- dictionary with the player and computer as keys and a list
    of card tuples as values
    deck -- list of card tuples
    card -- current top card tuple

    Returns:
    top_card -- new top card tuple

    Note:
    If the deck is exhausted turn the player's turn, the alternate_game_ending
    function is called.  This function does not return the expected card tuple,
    but this is handled in the play_crazy_eights function.
    """
    player_card_display(player, player_hands)
    card_index = is_play_valid(player, player_hands, card)
    while card_index == -1:
        try:
            player_hands[player].append(deck.pop())
        except IndexError:
            return alternate_game_ending(player_hands, player)
        player_card_display(player, player_hands)
        card_index = is_play_valid(player, player_hands, card)
    top_card = player_hands[player].pop(card_index)
    if len(player_hands[player]) == 0:
        return top_card
    if top_card[0] == 8:
        top_card = crazy_eight_player(top_card)
        print("{0} played a crazy eight!  The suit of the crazy eight is {1}.".format(player, top_card[1]))
    else:
        print("{0} played and the top card is now: {1} of {2}".format(player, top_card[0], top_card[1]))
    print("Computer's turn!")
    return top_card


def computer_turn(player_hands, deck, card):
    """Orchestrate steps of the computer's turn and return new top card tuple.

    Arguments:
    player_hands -- dictionary with the player and computer as keys and a list
    of card tuples as values
    deck -- list of card tuples
    card -- current top card tuple

    Returns:
    top_card -- new top card tuple

    Note:
    If the deck is exhausted turn the computer's turn, the alternate_game_ending
    function is called.  This function does not return the expected card tuple,
    but this is handled in the play_crazy_eights function.
    """
    go = 1
    while go == 1:
        suits_dict = {"Spades": 0, "Clubs": 0, "Diamonds": 0, "Hearts": 0}
        for index, comp_card in enumerate(player_hands['Computer']):
            if comp_card[1] == "Spades":
                suits_dict["Spades"] += 1
            if comp_card[1] == "Clubs":
                suits_dict["Clubs"] += 1
            if comp_card[1] == "Diamonds":
                suits_dict["Diamonds"] += 1
            if comp_card[1] == "Hearts":
                suits_dict["Hearts"] += 1
            if (comp_card[1] == card[1] or comp_card[0] == card[0]) and comp_card[0] != 8:
                top_card = player_hands['Computer'].pop(index)
                print("Computer played and the top card is now: {0} of {1}".format(
                    top_card[0], top_card[1]))
                print("Computer currently has {0} cards.".format(len(player_hands['Computer'])))
                return top_card
        for index, comp_card in enumerate(player_hands['Computer']):
            if comp_card[0] == 8:
                suits_dict[comp_card[1]] -= 1
                player_hands['Computer'].pop(index)
                max_suit = max(suits_dict, key=suits_dict.get)
                top_card = (8, max_suit)
                print("Computer played a crazy eight!  The suit of the crazy eight is {0}.".format(top_card[1]))
                return top_card
        print("Computer draws a card.")
        try:
            player_hands['Computer'].append(deck.pop())
        except IndexError:
            return alternate_game_ending(player_hands, player)

def play_crazy_eights(player, player_hands, deck, card):
    """Alternate play between player and computer and return game winner.

    Arguments:
    player -- inputed name of player
    player_hands -- dictionary with the player and computer as keys and a list
    of card tuples as values
    deck -- list of card tuples
    card -- current top card tuple

    Returns:
    winner -- string

    Note:
    If the alternate_game_ending function was called during computer_turn or
    player_turn, None was returned instead of a card tuple. To catch this, try
    and except is used to detect the expected TypeError and the program quits.
    """
    top_card = player_turn(player, player_hands, deck, card)
    game_continues = 1
    while game_continues == 1:
        top_card = computer_turn(player_hands, deck, top_card)
        try:
            x = top_card[0]
        except TypeError:
            quit()
        if len(player_hands['Computer']) == 0:
            winner = 'Computer'
            return winner
        top_card = player_turn(player, player_hands, deck, top_card)
        try:
            x = top_card[0]
        except TypeError:
            quit()
        if len(player_hands[player]) == 0:
            winner = player
            return winner


def calculate_points(player_hands):
    """Calculate hand totals and return the results in a dictionary."""
    results = {}
    for key, value in player_hands.items():
        points = 0
        for card in value:
            if card[0] == 8:
                points += 50
            elif card[0] in ("Jack", "Queen", "King"):
                points += 10
            elif card[0] == "Ace":
                points += 1
            else:
                points += card[0]
        results[key] = points
    return results


def alternate_game_ending(player_hands, player):
    """Determine winner if deck runs out of card tuples."""
    print("Since the deck ran out of cards, we will use points to determine the winner.")
    print("The player with the lowest number of points wins.")
    results_dict = calculate_points(player_hands)
    for key, value in results_dict.items():
        print("{0}, you earned {1} points.".format(key, value))
    if player_hands[player] < player_hands["Computer"]:
        print("{0} is the winner with {1} points! Congratulations!".format(player, player_hands[player]))
    elif player_hands[player] > player_hands["Computer"]:
        print("Computer is the winner with {0} points! Congratulations!".format(player_hands['Computer']))
    else:
        print("It's a tie!")
    return

# generate shuffled deck of cards
deck = list(itertools.product(
    ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'],
    ['Spades', 'Hearts', 'Diamonds', 'Clubs']))
random.shuffle(deck)

# alternate deck for game testing
"""
deck = list(itertools.product(
   [ 8, 9, 10, 'Jack', 'Queen', 'King']
   ['Spades', 'Hearts', 'Diamonds', 'Clubs']))
random.shuffle(deck)
"""
# method to make deck smaller for game testing
"""
for i in range(35):
    deck.pop()
"""

# initation of game, creation of player hands, reveal of intial top card
print("Welcome to Crazy Eights!")
player = input("Player, what is your name? ")

player_hands = {
    player: [deck.pop() for i in range(7)],
    'Computer': [deck.pop() for i in range(7)]
}

print("Dealing 7 cards each to {0} and Computer.".format(player))
print("Flipping over top card!")
print("{0} goes first.".format(player))
starter_card = deck.pop()
print("The top card is: {0} of {1}".format(starter_card[0], starter_card[1]))
if starter_card[0] == 8:
    player_card_display(player, player_hands)
    starter_card = crazy_eight_player(starter_card)
    print("Since the top card is a crazy eight, {0} choose {1} as the suit.".format(player, starter_card[1]))

# game play and winner declaration
winner = play_crazy_eights(player, player_hands, deck, starter_card)
print("The game is over!  Congratulations to the victor, {0}".format(winner))
