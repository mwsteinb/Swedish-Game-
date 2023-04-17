# dictionary to map the value of the card to its symbol
cardDict = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
}

# dictionary to map the suit value to the suit. A higher suit value goes first
suitDict = {
    0: "Spades",
    1: "Clubs",
    2: "Diamonds",
    3: "Hearts"
}


# Card class
# stores the value, symbol and other properties of a playing card in a class instance
class Card:
    def __init__(self, value, suit):
        self.value = value  # stores the value of the card for size comparison
        self.symbol = cardDict.get(value)   # symbol is used to display the card
        self.suit = suitDict.get(suit)   # suit defines the suit of the card and is used to determine who plays first

        # isSpecial defines if a card is special or not
        if value == 2 or value == 7 or value == 8 or value == 10 or value == 14:
            self.isSpecial = True
        else:
            self.isSpecial = False

    def __str__(self):
        return ' '.join([self.suit, self.value])
