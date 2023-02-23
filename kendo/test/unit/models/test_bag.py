import unittest

from actions.models.bag import Bag
from actions.models.hat import Hat
from actions.models.revolver import Revolver


class TestBag(unittest.TestCase):
    def test_check(self):
        bag = Bag()

        check = bag.check()

        self.assertEqual(check, [])

    def test_check_bag_with_hat(self):
        hat = Hat()        
        bag = Bag([hat])

        check = bag.check()

        self.assertEqual(check, [hat])

    def test_put(self):
        bag = Bag([])
        revolver = Revolver()

        bag.put(revolver)

        self.assertEqual(bag.check(), [revolver])

    def test_put_with_item(self):
        hat = Hat()
        bag = Bag([hat])
        revolver = Revolver()

        bag.put(revolver)

        self.assertCountEqual(bag.check(), [hat, revolver])

    def test_get(self):
        hat = Hat()
        revolver = Revolver()
        bag = Bag([hat, revolver])

        get = bag.get(Revolver)

        self.assertCountEqual(bag.check(), [hat])
        self.assertEqual(get, revolver)

    def test_get_without_item(self):
        hat = Hat()
        bag = Bag([hat])

        get = bag.get(Revolver)

        self.assertCountEqual(bag.check(), [hat])
        self.assertEqual(get, None)
