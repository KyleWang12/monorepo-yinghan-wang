from item import Item

class GeneralItem(Item):

    def update_quality(self):
        self.sell_in -= 1
        self.quality = max(0, self.quality - 1)