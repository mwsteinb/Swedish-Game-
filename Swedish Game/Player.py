from Card import Card


def sort(cards):
    done = False
    while not done:
        didSort = False
        for i in range(len(cards) - 1):
            if cards[i].value > cards[i+1].value:
                temp = cards[i]
                cards[i] = cards[i+1]
                cards[i+1] = temp
                didSort = True

        if not didSort:
            done = True

    return cards


class Player:
    bottomCards = []
    topCards = []
    handCards = []

    def __init__(self, bottomCards, topCards, handCards):
        self.bottomCards = bottomCards
        self.topCards = topCards
        self.handCards = handCards

    def sortCards(self):
        self.topCards = sort(self.topCards)
        self.handCards = sort(self.handCards)

    def getHandCardSymbols(self):
        cards = []
        for i in self.handCards:
            cards.append(i.symbol)
        return cards

    def getHandCardValues(self):
        cards = []
        for i in self.handCards:
            cards.append(i.value)
        return cards

    def getHandCards(self):
        cards = []
        for i in self.handCards:
            cards.append(i)
        return cards

    def getTopCardSymbols(self):
        cards = []
        for i in self.topCards:
            cards.append(i.symbol)
        return cards

    def getBottomCardSymbols(self):
        cards = []
        for i in self.bottomCards:
            cards.append(i.symbol)
        return cards

    def setHandCards(self, handCards):
        cards = []
        i = 0
        while i < len(handCards):
            cards.append(handCards[i])
            i = i + 1
        self.handCards = cards
