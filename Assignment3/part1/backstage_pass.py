from item import Item

class BackstagePass(Item):

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality = min(50, self.quality + 3)
        elif self.sell_in <= 10:
            self.quality = min(50, self.quality + 2)
        else:
            self.quality = min(50, self.quality + 1)