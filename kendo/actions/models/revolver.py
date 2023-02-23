
class Revolver:
    _MAX_AMMO = 6
    _AMMO_PER_SHOT = 1

    def __init__(self, ammo=_MAX_AMMO):        
        self._ammo = ammo

    def verificar_cartucho(self):
        return self._ammo

    def reload(self):
        if self._ammo == self._MAX_AMMO:
            return False
        elif self._ammo < self._MAX_AMMO:
            self._ammo = self._MAX_AMMO
            return True

    def shoot(self):
        if self._ammo:
            self._ammo -= self._AMMO_PER_SHOT
            return True
        else:
            return False
