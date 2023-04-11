class Deck:

    def __init__(self, cards):
        self._cards = [cards]
        self.size = len(self.cards)

    @property
    def cards(self):
        return self._cards

    def build(self):
        pass

    def show(self):
        pass

    def shuffle(self):
        pass

    def draw(self):
        pass

    def add(self):
        pass 