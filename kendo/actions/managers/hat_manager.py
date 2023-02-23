from ..models.hat import Hat


class HatManager:
    GOTTEN_FROM_BAG = 'gotten_from_bag'
    PUT_IN_BAG = 'put_in_bag'
    WEARING_HAT = 'wearing_hat'
    NO_HAT = 'no_hat'
    HAT_IN_BAG =  'hat_in_bag'

    def __init__(self, pessoa):
        self._pessoa = pessoa

    @property
    def _head(self):
        return self._pessoa.head

    @property
    def _bag(self):
        return self._pessoa.bag

    def equip_hat(self):
        # apenas um tipo de return
        hat = self._bag.get(Hat)
        if hat:
            self._head.equip_item(hat)
            return self.GOTTEN_FROM_BAG
        elif self._head.equipped:
            return self.WEARING_HAT
        else:
            return self.NO_HAT

    def _has_hat_in_bag(self):
        for item in self._bag.check():
            if type(item) == Hat:
                return True

    def unequip_hat(self):
        # apenas um tipo de return
        if self._head.equipped:
            item = self._head.unequip_item()
            self._bag.put(item)
            return self.PUT_IN_BAG
        elif self._has_hat_in_bag():
            return self.HAT_IN_BAG
        else:
            return self.NO_HAT
