class BouncyBall:

    def __init__(self, price):
        self._price = price


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price too low!")