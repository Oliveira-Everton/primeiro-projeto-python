import unittest

from actions.managers.hat_manager import HatManager
from actions.serializers.output_serializer import OutputSerializer
from actions.managers.revolver_manager import RevolverManager


class TestOutputSerializer(unittest.TestCase):
    def test_output_string_getting_revolver(self):
        output_string = OutputSerializer().output_string(
            'pegando',
            'revolver',
            RevolverManager.GOTTEN_FROM_BAG
        )

        self.assertEqual(output_string, 'Peguei o revólver')

    def test_output_string_putting_revolver(self):
        output_string = OutputSerializer().output_string(
            'guardando',
            'revolver',
            RevolverManager.PUT_IN_BAG
        )

        self.assertEqual(output_string, 'Guardei o revólver')

    def test_output_string_getting_hat(self):
        output_string = OutputSerializer().output_string(
            'pegando',
            'hat', 
            HatManager.GOTTEN_FROM_BAG
        )

        self.assertEqual(output_string, 'Botei o chapéu')

    def test_output_string_putting_hat(self):
        output_string = OutputSerializer().output_string(
            'guardando',
            'hat',
            HatManager.PUT_IN_BAG
        )

        self.assertEqual(output_string, 'Guardei o chapéu')

    def test_output_string_getting_revolver_already_with_it(self):
        output_string = OutputSerializer().output_string(
            'pegando',
            'revolver',
            RevolverManager.HOLDING_REVOLVER
        )

        self.assertEqual(output_string, 'Já tá na mão uai')

    def test_output_string_getting_hat_already_with_it(self):
        output_string = OutputSerializer().output_string(
            'pegando',
            'hat',
            HatManager.WEARING_HAT
        )

        self.assertEqual(output_string, 'Já estou com ele')

    def test_output_string_equip_hat_without_hat(self):
        output_string = OutputSerializer().output_string(
            'pegando',
            'hat',
            HatManager.NO_HAT
        )

        self.assertEqual(output_string, 'Nem tenho chapéu uai')
