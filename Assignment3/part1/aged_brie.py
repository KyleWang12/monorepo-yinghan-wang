from item import Item

class AgedBrie(Item):

    def update_quality(self):
        self.sell_in -= 1
        self.quality = min(50, self.quality + 1)


