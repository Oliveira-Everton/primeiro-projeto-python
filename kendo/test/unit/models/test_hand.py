import unittest

from actions.models.hand import Hand
from actions.models.revolver import Revolver
from actions.models.bag import Bag


class TestHand(unittest.TestCase):
    def test_hold(self):
        hand = Hand()
        revolver = Revolver()

        hand.hold(revolver)

        self.assertEqual(hand.equipped, revolver)

    def test_drop(self):
        hand = Hand()
        revolver = Revolver()
        hand.hold(revolver)

        drop = hand.drop()

        self.assertEqual(hand.equipped, None)
        self.assertEqual(drop, revolver)

    def test_shoot(self):
        hand = Hand()
        revolver = Revolver()
        hand.hold(revolver)

        shoot = hand.shoot()

        self.assertEqual(shoot, True)

    def test_shoot_without_gun(self):
        hand = Hand()

        shoot = hand.shoot()

        self.assertEqual(shoot, False)

    def test_shoot_revolver_in_bag(self):
        hand = Hand()
        bag = Bag([Revolver()])
        item = bag.get(Revolver)
        hand.hold(item)

        shoot = hand.shoot()

        self.assertEqual(shoot, True)
