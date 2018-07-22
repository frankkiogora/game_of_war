# ***War Game***
# War is a card game designed for two players, utilizing a standard (French style) 52-card deck of playing-cards. The objective is to "capture" all the cards in the game before your opponent.
# *Gameplay*
# All cards are shuffled, and then divided equally to each player in face down stacks (one stack for each player). Each player reveals the top card of their deck simultaneously, with the player revealing the highest-ranking card winning that particular round and thusly "capturing" their opponent's card (in addition to retaining their card). Both cards are then returned to the round-winner's deck, placed face down at the bottom. Gameplay continues in the above fashion, with players playing out consecutive rounds, until one player runs out of cards and loses.
# *Rankings*
# Cards are ranked by face value, with Ace, King, Queen, and Jack each (in order) taking the highest ranking, followed by number cards in numerical order (10 being worth more than a 9, etc.). Output must show face value and suite of the card.
# *Ties*
# In the event of a tie in a round - two players playing the same ranked cards - both cards are left face up between the two players, and play proceeds to the next round. The winner of the next round takes all cards from the current as well as previous round.
# *Challenge*
# Your challenge is to write an application to simulate a game of War. Play out a game in full, and output the winner. Additionally, outputting the results of each round, including the card that each player played as well as the verdict of which player won. If no winner exists after 100 rounds, the game ends with a prompt to play chess instead.
# print ("hello")








from enum import Enum
from enum import IntEnum
from random import randint

full_deck = []
partial_deck = []
player_One_cards = []
player_two_cards = []

# Card enum for playing cards


class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

# Suit enum for playing cards


class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

# Class to hold information for playing cards


class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

#  Function to deal full deck of cards


def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck

# Draw single card from "deck"


def draw_card(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)

# Deal two players


def deal_war():

    while (len(partial_deck) > 0):
        player_One_cards.append(draw_card(partial_deck))
        player_two_cards.append(draw_card(partial_deck))
create_deck()

# Leaves "full_deck" unchanged and unshuffled

partial_deck = list(full_deck)
deal_war()
rounds = 0

for i in range(0, len(player_One_cards)):
    rounds += 1
    print ' NUMBER OF ROUNDS PLAYED # ', rounds
  

    if (player_One_cards[i].card == player_two_cards[i].card):
        
        print 'War War War War !!!!!!', player_One_cards[i].card, player_two_cards[i].card

        print ' ###########################################'

    if(player_One_cards[i].card > player_two_cards[i].card):
        print "Player One wins the hand with :", player_One_cards[i].card
        print "Player Two loses with :", player_two_cards[i].card
        player_One_cards.extend([player_One_cards[i].card+player_two_cards[i].card])
       

        print ' ###########################################'

    if(player_One_cards[i].card < player_two_cards[i].card):
        player_two_cards.extend([player_two_cards[i].card+player_One_cards[i].card])
        print "Player Two wins the hand with : ", player_two_cards[i].card
        print "Player One loses with : ", player_One_cards[i].card

        print ' ###########################################'
