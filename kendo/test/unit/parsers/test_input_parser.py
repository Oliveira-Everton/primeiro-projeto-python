import unittest

from actions.parsers.input_parser import InputParser
from actions.models.pessoa import Pessoa
from actions.models.bag import Bag
from actions.models.revolver import Revolver



class TestInputParser(unittest.TestCase):
    def test_execute_command_get_revolver(self):
        pessoa = Pessoa(bag=Bag([Revolver()]))

        output_string = InputParser(pessoa).execute_command('pegar revólver')

        self.assertEqual(output_string, 'Peguei o revólver')
