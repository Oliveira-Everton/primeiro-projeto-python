from ..models.revolver import Revolver


class RevolverManager:
    GOTTEN_FROM_BAG = 'gotten_from_bag'
    HOLDING_REVOLVER = 'holding_revolver'
    NO_REVOLVER = 'no_revolver'
    PUT_IN_BAG = 'put_in_bag'
    REVOLVER_IN_BAG = 'revolver_in_bag'

    def __init__(self, pessoa):
        self._pessoa = pessoa
  
    @property
    def _hand(self):
        return self._pessoa.hand

    @property
    def _bag(self):
        return self._pessoa.bag

    def get_revolver(self):
        # apenas um tipo de return
        revolver = self._bag.get(Revolver)
        if revolver:
            self._hand.hold(revolver)
            return self.GOTTEN_FROM_BAG
        elif self._hand.equipped:
            return self.HOLDING_REVOLVER
        else:
            return self.NO_REVOLVER

    def _has_revolver_in_bag(self):
        for item in self._bag.check():
            if type(item) == Revolver:
                return True

    def put_revolver(self):
        # apenas um tipo de return
        if self._hand.equipped:
            item = self._hand.drop()
            self._bag.put(item)
            return self.PUT_IN_BAG
        elif self._has_revolver_in_bag():
            return self.REVOLVER_IN_BAG
        else:
            return self.NO_REVOLVER
