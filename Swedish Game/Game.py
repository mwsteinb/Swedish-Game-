import random
from Player import Player
from Card import Card


class Game:
    drawPile = []     # draw pile player draw cards from
    dropPile = []     # drop pile where cards are played to
    discardPile = []  # discard pile cards are discarded to when cleared
    players = []      # ordered list of players and the play order
    numPlayers = 0    # number of players in the game

    def __init__(self, numPlayers):
        # create the deck of cards. 2 is the lowest card and 14 is the highest (Ace)
        # four of each value for the four suits in a standard deck
        for i in range(2, 15):
            for j in range(4):
                self.drawPile.append(Card(i, j))
        random.shuffle(self.drawPile)  # shuffle cards before starting game

        self.numPlayers = numPlayers  # define the number of players in the game

        # deal cards to each player in the game
        for i in range(self.numPlayers):
            bottomCards = []
            topCards = []
            handCards = []

            # deal three cards for top, bottom, and hand cards
            for j in range(3):
                bottomCards.append(self.drawPile.pop())
                topCards.append(self.drawPile.pop())
                handCards.append(self.drawPile.pop())

            player = Player(bottomCards, topCards, handCards)  # create Player instance and assign cards
            player.sortCards()  # sort the cards
            self.players.append(player)  # add player to player list


    def canPlay(self, cardValue):
        if len(self.dropPile) == 0 or cardValue == 10 or cardValue == 2:
            return True
        else:
            topCard = self.dropPile[0]
            if topCard.value == 7 and cardValue >= 7:
                return False
            elif cardValue >= topCard.value:
                return True
            else:
                return False

    def start(self):
        print("Welcome to Swedish Game!")
        print(self.dropPile)
        print("Player 1 turn:")
        self.playCard(self.getInput(0))

        while len(self.drawPile) > 0:
            for i in range(self.numPlayers):
                print(self.dropPile)
                print("Player %d turn:" %i)
                self.playCard(self.getInput(i))

    def getInput(self, playerNum):
        handCards = self.players[playerNum].getHandCardSymbols()
        while True:
            print(handCards)
            inp = input("Choose a card to play: ")
            if inp.isdigit():
                inp = int(inp)
                if not (inp in handCards):
                    print("Please select a card in your hand")
                elif not self.canPlay(inp):
                    print("That card cannot be played")
                else:
                    break
            else:
                print("Please select a card in your hand")

        cards = []
        while handCards.count(inp) >= 1:
            index = handCards.index(inp)
            cards.append(handCards.pop(index))

        while len(handCards) < 3:
            handCards.append(self.drawPile.pop())

        self.players[playerNum].setHandCardValues(handCards)
        self.players[playerNum].sortCards()

        return cards

    def playCard(self, cards):
        for i in cards:
            self.dropPile.insert(0, i)


"""
        for i in self.players:
            i.showHand()
            i.showTopCards()
            i.showBottomCards()
"""
