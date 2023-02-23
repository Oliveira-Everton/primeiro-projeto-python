import unittest

from actions.models.hat import Hat
from actions.managers.hat_manager import HatManager
from actions.models.pessoa import Pessoa
from actions.models.bag import Bag
from actions.models.head import Head


class TestHatManager(unittest.TestCase):
    def test_equip_hat(self):
        hat = Hat()
        pessoa = Pessoa(bag=Bag([hat]), head=Head())

        equip_hat = HatManager(pessoa).equip_hat()

        self.assertEqual(equip_hat, 'gotten_from_bag')
        self.assertEqual(pessoa.head.equipped, hat)

    def test_equip_hat_with_hat(self):
        pessoa = Pessoa(head=Head(Hat()), bag=Bag([]))

        equip_hat = HatManager(pessoa).equip_hat()

        self.assertEqual(equip_hat, 'wearing_hat')

    def test_equip_hat_without_hat(self):
        pessoa = Pessoa(head=Head(), bag=Bag([]))

        equip_hat = HatManager(pessoa).equip_hat()

        self.assertEqual(equip_hat, 'no_hat')

    def test_unequip_hat(self):
        hat = Hat()
        pessoa = Pessoa(head=Head(hat), bag=Bag([]))

        put_hat = HatManager(pessoa).unequip_hat()

        self.assertEqual(put_hat, 'put_in_bag')
        self.assertEqual(pessoa.bag.check(), [hat])

    def test_unequip_hat_with_unequipped_hat(self):
        pessoa = Pessoa(head=Head(), bag=Bag([Hat()]))

        put_hat = HatManager(pessoa).unequip_hat()

        self.assertEqual(put_hat, 'hat_in_bag')

    def test_unequip_hat_without_hat(self):
        pessoa = Pessoa(head=Head(), bag=Bag([]))

        put_hat = HatManager(pessoa).unequip_hat()

        self.assertEqual(put_hat, 'no_hat')
