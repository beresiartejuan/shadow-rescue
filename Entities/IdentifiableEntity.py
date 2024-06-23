from Entities.EntityWithItems import EntityWithItems
from uuid import uuid4


class IdentifiableEntity(EntityWithItems):

    def __init__(self, *, health: int = 0, attack: int = 0, energy: int = 0) -> None:
        super().__init__(health=health, attack=attack, energy=energy)
        self.id = uuid4()
        self.role: str = "NPC"
