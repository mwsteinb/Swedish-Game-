import random
from Player import *
from Card import *
hello


class Game:
    drawPile = []  # draw pile player draw cards from
    dropPile = []  # drop pile where cards are played to
    discardPile = []  # discard pile cards are discarded to when cleared
    players = []  # ordered list of players and the play order
    numPlayers = 0  # number of players in the game
    turn = 0  # index of player whose turn it is

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

    def start(self):
        print("Welcome to Swedish Game!")
        while len(self.drawPile) > 0:
            print("Cards remaining " + str(len(self.drawPile)))
            print("Drop Pile:", end=" ")
            for i in self.dropPile:
                print(i.symbol, end=" ")
            print("\nPlayer " + str(self.turn) + " turn:")
            cards = self.getInput(self.turn)
            self.playCard(cards)
            if cards[0] == 'p':
                while len(self.dropPile) > 0:
                    self.players[self.turn].handCards.append(self.dropPile.pop(0))
                    self.players[self.turn].sortCards()
                self.turn += 1
            elif cards[0].is8:
                self.turn += 2
            elif cards[0].is10:
                self.discardPile.append(self.dropPile)
                self.dropPile = []
            else:
                self.turn += 1

            self.turn = self.turn % self.numPlayers

    def canPlay(self, card):
        if len(self.dropPile) == 0 or card.value == 10 or card.value == 2:
            return True
        else:
            topCard = self.dropPile[0]
            if topCard.value == 7 and card.value <= 7:
                return True
            elif card.value >= topCard.value:
                return True
            else:
                return False

    def getInput(self, playerNum):
        # grabs symbols and values from players hand
        handCards = self.players[playerNum].getHandCards()
        # input validation loop
        while True:
            i = 0
            while i < len(handCards):
                print(handCards[i].symbol, end=" ")
                i = i + 1
            inp = input("\nChoose a card to play by position (e.g. 1, 2, 3) or p (to pickup): ")
            if inp == 'p':
                return ['p']
            elif len(handCards) >= int(inp) > 0:
                # fix idx bounds
                inp = int(inp) - 1
                # check if card at entered index can be played
                if not self.canPlay(handCards[inp]):
                    print("That card cannot be played")
                else:
                    break
            else:
                print("Please select a card in your hand")

        inpval = handCards[inp].value
        cards = [card for card in handCards if card.value == inpval]
        for card in cards:
            handCards.remove(card)

        while len(handCards) < 3:
            drawcard = self.drawPile.pop()
            handCards.append(drawcard)

        self.players[playerNum].setHandCards(handCards)
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
