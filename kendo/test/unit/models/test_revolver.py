import unittest

from actions.models.revolver import Revolver

class TestRevolver(unittest.TestCase):
    def test_verificar_cartucho(self):
        revolver = Revolver(6)

        check_ammo = revolver.verificar_cartucho()

        self.assertEqual(check_ammo, 6)

    def test_reload_with_full_magazine(self):
        revolver = Revolver(6)

        reload_revolver = revolver.reload()

        self.assertEqual(reload_revolver, False)

    def test_reload_with_half_magazine(self):
        revolver = Revolver(3)

        reload_revolver = revolver.reload()

        self.assertEqual(reload_revolver, True)
        self.assertEqual(revolver._ammo, 6)

    def test_shoot(self):
        revolver = Revolver(2)

        shoot_revolver = revolver.shoot()

        self.assertEqual(shoot_revolver, True)
        self.assertEqual(revolver._ammo, 1)

    def test_shoot_no_ammo(self):
        revolver = Revolver(0)

        shoot_revolver = revolver.shoot()

        self.assertEqual(shoot_revolver, False)
