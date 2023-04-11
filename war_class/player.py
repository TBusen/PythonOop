class Player:

    def __init__(self, name:str, deck:Deck, is_computer:bool):

        self.name= name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def deck(self):
        return self._deck    


    def has_empty_deck(self):
        if self.deck.size == 0:
            return True
        else:
            return False


    def add_card(self):
        pass
            

