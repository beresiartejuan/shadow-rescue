from Items.Item import Item
from Effects.HealthEffect import HealthEffect


class Bread(Item):

    def __init__(self):
        super().__init__(name="Pan", attack=0, defense=0, uses=1)
        self.setEffect(HealthEffect(health=15))
