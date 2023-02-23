class Hand:
    def __init__(self, item=None):
        self._item = item

    @property
    def equipped(self):
        return self._item

    def hold(self, item):
        self._item = item

    def drop(self):
        item = self._item
        self._item = None
        return item

    def shoot(self):
        if self._item:
            return self._item.shoot()
        else:
            return False
