class Bag:
    def __init__(self, inventory=[]):
        self._inventory = inventory

    def check(self):
        return self._inventory

    def put(self, item):
        self._inventory.append(item)

    def get(self, item_class):
        for item in self._inventory:
            if type(item) == item_class:
                self._inventory.remove(item)
                return item
