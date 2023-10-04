# -*- coding: utf-8 -*-
from sulfuras import Sulfuras
from aged_brie import AgedBrie
from backstage_pass import BackstagePass
from conjured import Conjured
from general_item import GeneralItem
from item import Item

class GildedRose(object):

    _my_classes = {
        "Sulfuras": Sulfuras,
        "Aged Brie": AgedBrie,
        "Backstage pass": BackstagePass,
        "Conjured": Conjured
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def _get_cls(self, name):
        for key in self._my_classes:
            if key.lower() in name.lower():
                return self._my_classes[key]
        return GeneralItem


    def update_quality(self):
        for item in self.items:
            item.__class__ = self._get_cls(item.name)
            item.update_quality()
