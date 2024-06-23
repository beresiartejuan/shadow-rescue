from typing import List
from typing_extensions import Self
from Entities.IdentifiableEntity import IdentifiableEntity
from Items.Item import Item


class Room:

    def __init__(self, label: str):
        self.entities: List[IdentifiableEntity] = []
        self.objects: List[Item] = []
        self.directions: List[Self] = []
        self.label: str = label
        self.descriptions: List[str] = []
        self.energy_cost: int = 0
        self.ambiental_damage = 0

    def add_entity(self, entity: IdentifiableEntity):
        self.entities.append(entity)

    def add_object(self, object: Item):
        self.objects.append(object)

    def add_description(self, description: str):
        self.descriptions.append(description)

    def add_direction(self, room: Self):
        self.directions.append(room)

    def playerIsHere(self):
        for e in self.entities:
            if e.role == "player":
                return True

        return False
