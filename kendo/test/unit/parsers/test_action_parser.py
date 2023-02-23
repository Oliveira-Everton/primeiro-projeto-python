import unittest

from actions.models.hat import Hat
from actions.models.head import Head
from actions.models.pessoa import Pessoa
from actions.parsers.action_parser import ActionParser
from actions.models.revolver import Revolver
from actions.models.bag import Bag
from actions.models.hand import Hand


class TestActionParser(unittest.TestCase):
    def test_find_command_get_revolver_successfully(self):
        pessoa = Pessoa(bag=Bag([Revolver()]))

        find_command = ActionParser('get', 'revolver', pessoa).find_command()

        self.assertEqual(find_command, 'Peguei o revólver')

    def test_find_command_get_hat_successfully(self):
        hat = Hat()
        pessoa = Pessoa(bag=Bag([hat]), head=Head())

        find_command = ActionParser('get', 'hat', pessoa).find_command()

        self.assertEqual(find_command, 'Botei o chapéu')

    def test_find_command_put_revolver(self):
        revolver = Revolver()
        pessoa = Pessoa(hand=Hand(revolver), bag=Bag([])) 
        action_parser = ActionParser('put', 'revolver', pessoa)

        find_command = action_parser.find_command()

        self.assertEqual(find_command, 'Guardei o revólver')

    def test_find_command_put_hat(self):
        hat = Hat()
        pessoa = Pessoa(head=Head(hat), bag=Bag([]))
        action_parser = ActionParser('put', 'hat', pessoa)

        find_command = action_parser.find_command()

        self.assertEqual(find_command, 'Guardei o chapéu')
