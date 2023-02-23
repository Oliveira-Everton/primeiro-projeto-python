import unittest

from actions.parsers.input_parser import InputParser
from actions.models import (
    Bag,
    Hand,
    Hat,
    Head,
    Pessoa,
    Revolver
)


class TestIntegration(unittest.TestCase):
    def test_command_get_revolver(self):
        revolver = Revolver()
        hat = Hat()
        pessoa = Pessoa(bag=Bag([revolver, hat]), head=Head(), hand=Hand())
        
        output_string = InputParser(pessoa).execute_command('pegar revólver')

        self.assertEqual(output_string, 'Peguei o revólver')

    def test_command_get_revolver_without_revolver(self):
        pessoa = Pessoa(bag=Bag([]), hand=Hand())

        output_string = InputParser(pessoa).execute_command('get revolver')

        self.assertEqual(output_string, 'Nem tenho revólver uai')
        self.assertEqual(pessoa.bag.check(), [])
        self.assertEqual(pessoa.hand.equipped, None)

    def test_command_get_revolver_without_revolver_and_hat_in_bag(self):
        hat = Hat()
        pessoa = Pessoa(bag=Bag([hat]), hand=Hand())

        output_string = InputParser(pessoa).execute_command('get revolver')

        self.assertEqual(output_string, 'Nem tenho revólver uai')
        self.assertEqual(pessoa.bag.check(), [hat])
        self.assertEqual(pessoa.hand.equipped, None)

    def test_command_get_revolver_already_with_it(self):
        revolver = Revolver()
        hat = Hat()
        pessoa = Pessoa(hand=Hand(revolver), bag=Bag([]), head=Head(hat))
        
        output_string = InputParser(pessoa).execute_command('pegar revólver')

        self.assertEqual(output_string, 'Já tá na mão uai')
        self.assertEqual(pessoa.hand.equipped, revolver)
        self.assertEqual(pessoa.bag.check(), [])
        self.assertEqual(pessoa.head.equipped, hat)

    def test_command_put_revolver(self):
        revolver = Revolver()
        hat = Hat()
        pessoa = Pessoa(hand=Hand(revolver), bag=Bag([hat]))

        output_string = InputParser(pessoa).execute_command('guardar revólver')

        self.assertEqual(output_string, 'Guardei o revólver')
        self.assertEqual(pessoa.hand.equipped, None)
        self.assertEqual(pessoa.bag.check(), [hat, revolver])

    def test_command_put_revolver_with_it_in_bag(self):
        revolver = Revolver()
        hat = Hat()
        pessoa = Pessoa(hand=Hand(), bag=Bag([revolver]), head=Head(hat))

        output_string = InputParser(pessoa).execute_command('guardar revólver')

        self.assertEqual(output_string, 'Já está guardado uai')
        self.assertEqual(pessoa.hand.equipped, None)
        self.assertEqual(pessoa.bag.check(), [revolver])
        self.assertEqual(pessoa.head.equipped, hat)

    def test_command_equip_hat(self):
        hat = Hat()
        revolver = Revolver()
        pessoa = Pessoa(bag=Bag([hat, revolver]), head=Head())

        output_string = InputParser(pessoa).execute_command('pegar chapéu')

        self.assertEqual(output_string, 'Botei o chapéu')
        self.assertEqual(pessoa.bag.check(), [revolver])
        self.assertEqual(pessoa.head.equipped, hat)

    def test_command_equip_hat_without_hat_and_revolver_in_bag(self):
        hat = Hat()
        revolver = Revolver()
        pessoa = Pessoa(head=Head(hat), bag=Bag([revolver]))

        output_string = InputParser(pessoa).execute_command('pegar chapéu')

        self.assertEqual(output_string, 'Já estou com ele')
        self.assertEqual(pessoa.head.equipped, hat)
        self.assertEqual(pessoa.bag.check(), [revolver])

    def test_command_put_hat(self):
        revolver = Revolver()
        hat = Hat()
        pessoa = Pessoa(head=Head(hat), bag=Bag([]), hand=Hand(revolver))

        output_string = InputParser(pessoa).execute_command('guardar chapéu')

        self.assertEqual(output_string, 'Guardei o chapéu')
        self.assertEqual(pessoa.bag.check(), [hat])
        self.assertEqual(pessoa.hand.equipped, revolver)

    def test_command_put_hat_with_it_in_bag(self):
        revolver = Revolver()
        hat = Hat()
        pessoa = Pessoa(head=Head(), bag=Bag([hat, revolver]), hand=Hand())

        output_string = InputParser(pessoa).execute_command('guardar chapéu')

        self.assertEqual(output_string, 'Já está guardado')
        self.assertEqual(pessoa.hand.equipped, None)
        self.assertEqual(pessoa.head.equipped, None)
        self.assertEqual(pessoa.bag.check(), [hat,revolver])

    def test_command_put_hat_without_hat_and_revolver_equipped(self):
        revolver = Revolver()
        pessoa = Pessoa(head=Head(), bag=Bag([]), hand=Hand(revolver))

        output_string = InputParser(pessoa).execute_command('guardar chapéu')

        self.assertEqual(output_string, 'Nem tenho chapéu uai')
        self.assertEqual(pessoa.hand.equipped, revolver)
        self.assertEqual(pessoa.head.equipped, None)
        self.assertEqual(pessoa.bag.check(), []) 
