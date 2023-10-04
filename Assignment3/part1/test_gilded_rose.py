# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item

class GildedRoseTest(unittest.TestCase):

    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured sdf", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = items[0].sell_in
        original_quality = items[0].quality

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = items[0].sell_in
        new_quality = items[0].quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2

    # Test for "Aged Brie"
    def test_aged_brie(self):
        items = [Item("Aged Brie asdf", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = items[0].sell_in
        original_quality = items[0].quality

        gr.update_quality()

        self.assertEqual(items[0].sell_in, original_sell_in - 1)
        self.assertEqual(items[0].quality, original_quality + 1)
        self.assertTrue(items[0].quality <= 50)

    # Test for "Sulfuras"
    def test_sulfuras(self):
        items = [Item("Sulfuras sdf", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = items[0].sell_in
        original_quality = items[0].quality

        gr.update_quality()

        self.assertEqual(items[0].sell_in, original_sell_in)
        self.assertEqual(items[0].quality, original_quality)

    # Test for "Backstage passes"
    def test_backstage_passes(self):
        # More than 10 days left
        items = [Item("Backstage passes sdfksdklfj", 15, 42)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 43)  # Increases by 1
        self.assertEqual(items[0].sell_in, 14)

        # 10 days or less but more than 5 days
        items = [Item("Backstage passes sdfksdklfj", 10, 42)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 44)  # Increases by 2
        self.assertEqual(items[0].sell_in, 9)

        # 5 days or less but more than 0 days
        items = [Item("Backstage passes sdfksdklfj", 5, 42)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 45)  # Increases by 3
        self.assertEqual(items[0].sell_in, 4)

        # The day of the concert
        items = [Item("Backstage passes sdfksdklfj", 1, 42)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 45)  # Increases by 3
        self.assertEqual(items[0].sell_in, 0)

        # After the concert
        items = [Item("Backstage passes sdfksdklfj", 0, 42)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)  # Drops to 0
        self.assertEqual(items[0].sell_in, -1)


        
        

if __name__ == '__main__':
    unittest.main()
