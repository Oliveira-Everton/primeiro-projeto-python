import unittest

from actions.models.head import Head
from actions.models.hat import Hat


class TestHead(unittest.TestCase):
    def test_equipped(self):
        head = Head()

        self.assertEqual(head.equipped, None)

    def test_equipped_with_hat(self):
        hat = Hat()
        head = Head(hat)

        self.assertEqual(head.equipped, hat)

    def test_equip_item(self):
        head = Head()
        hat = Hat()

        head.equip_item(hat)

        self.assertEqual(head.equipped, hat)

    def test_unequip_item(self):
        head = Head()
        hat = Hat()
        head.equip_item(hat)

        unequip = head.unequip_item()

        self.assertEqual(head.equipped, None)
        self.assertEqual(unequip, hat)

    def test_unequip_item_without_item(self):
        head = Head()

        unequip = head.unequip_item()

        self.assertEqual(unequip, None)
        self.assertEqual(head.equipped, None)
