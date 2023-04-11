class Suit:

    SUIT_DESCRIPTIONS = {"club": "♣",  "diamond":"♦",  "heart":"♥", "spade":"♠"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SUIT_DESCRIPTIONS.get(description.lower())

        @property
        def description(self):
            return self._description

        @property
        def symbol(self):
            return self._symbol