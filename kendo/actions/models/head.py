class Head:
    def __init__(self, item=None):
        self._item = item

    @property
    def equipped(self):
        return self._item

    def equip_item(self, item):
        self._item = item

    def unequip_item(self):
        item = self._item
        self._item = None
        return item
