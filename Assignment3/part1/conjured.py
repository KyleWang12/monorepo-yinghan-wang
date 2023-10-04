from item import Item

class Conjured(Item):

    def update_quality(self):
        self.sell_in -= 1
        self.quality = max(0, self.quality - 2)