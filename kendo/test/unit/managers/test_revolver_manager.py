import unittest

from actions.managers.revolver_manager import RevolverManager
from actions.models.pessoa import Pessoa
from actions.models.revolver import Revolver
from actions.models.bag import Bag
from actions.models.hand import Hand
from actions.models.hat import Hat


class TestRevolverManager(unittest.TestCase):
    def test_get_revolver(self):
        revolver = Revolver()
        pessoa = Pessoa(bag=Bag([revolver]), hand=Hand())

        get_revolver = RevolverManager(pessoa).get_revolver()

        self.assertEqual(get_revolver, 'gotten_from_bag')
        self.assertEqual(pessoa.hand.equipped, revolver)
        self.assertEqual(pessoa.bag.check(), [])

    def test_get_revolver_with_revolver_equipped(self):
        revolver = Revolver()
        pessoa = Pessoa(hand=Hand(revolver), bag=Bag([]))

        get_revolver = RevolverManager(pessoa).get_revolver()

        self.assertEqual(get_revolver, 'holding_revolver')
        self.assertEqual(pessoa.hand.equipped, revolver)
        self.assertEqual(pessoa.bag.check(), [])

    def test_get_revolver_without_revolver(self):
        pessoa = Pessoa(bag=Bag([]), hand=Hand())

        get_revolver = RevolverManager(pessoa).get_revolver()

        self.assertEqual(get_revolver, 'no_revolver')
        self.assertEqual(pessoa.hand.equipped, None)

    def test_put_revolver(self):
        revolver = Revolver()
        pessoa = Pessoa(bag=Bag([]), hand=Hand(revolver))

        put_revolver = RevolverManager(pessoa).put_revolver()

        self.assertEqual(put_revolver, 'put_in_bag')
        self.assertEqual(pessoa.hand.equipped, None)
        self.assertEqual(pessoa.bag.check(), [revolver])

    def test_put_revolver_with_unequipped_revolver(self):
        revolver = Revolver()
        pessoa = Pessoa(bag=Bag([revolver]), hand=Hand())

        put_revolver = RevolverManager(pessoa).put_revolver()

        self.assertEqual(put_revolver, 'revolver_in_bag')
        self.assertEqual(pessoa.bag.check(), [revolver])
        self.assertEqual(pessoa.hand.equipped, None)

    def test_put_revolver_without_revolver(self):
        pessoa = Pessoa(bag=Bag([]), hand=Hand())

        put_revolver = RevolverManager(pessoa).put_revolver()

        self.assertEqual(put_revolver, 'no_revolver')
        self.assertEqual(pessoa.bag.check(), [])

    def test_put_revolver_without_revolver_and_hat_in_bag(self):
        hat = Hat()
        pessoa = Pessoa(bag=Bag([hat]), hand=Hand())

        put_revolver = RevolverManager(pessoa).put_revolver()

        self.assertEqual(put_revolver, 'no_revolver')
        self.assertEqual(pessoa.bag.check(), [hat])
