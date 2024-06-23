from Items.Item import Item


class Axe(Item):

    def __init__(self):
        super().__init__(name="Hacha", attack=15, defense=1, uses=15)
