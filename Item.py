from Entity import Entity
from Effect import Effect
from typing import List


class Item:

    def __init__(self, *, name: str, attack: int, defense: int, uses: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.uses = uses
        self.effects: List[Effect] = []

    def setEffect(self, effect: Effect):
        self.effects.append(effect)

    def use(self, entity: Entity) -> None:
        self.uses -= 1

        for effect in self.effects:
            effect.use(entity=entity)

    def __str__(self) -> str:
        return f"[{self.name}] ({self.uses} usos restantes)"
