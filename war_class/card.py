class Card:

    SPECIAL_MAP = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self, value):
        return self.value >= 11

    def show(self):

        card_value = self.value
        card_description = self.suit.description.capitalize()
        card_symbol = self.suit.symbol

        if not self.is_special(self.value):
            print(f"{card_value} of {card_description} {card_symbol}")
        else:
            special_card = Card.SPECIAL_MAP.get(card_value)
            print(f"{special_card} of {card_description} {card_symbol}")