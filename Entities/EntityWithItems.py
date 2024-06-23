from typing import List
from Items.Item import Item
from Entities.Entity import Entity


class EntityWithItems(Entity):

    def __init__(self, *, health: int = 0, attack: int = 0, energy: int = 0) -> None:
        super().__init__(health=health, attack=attack, energy=energy)
        self.items: List[Item] = []

    def get_damage(self, damage: int) -> None:
        for item in self.items:
            damage -= item.defense

        return super().get_damage(damage=damage)

    def add_item(self, item: Item) -> bool:
        if len(self.items) >= 4:
            return False

        self.items.append(item)
        return True
