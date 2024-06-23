from Entities.IdentifiableEntity import IdentifiableEntity
from Rooms.Room import Room


class MovableEntity(IdentifiableEntity):

    def __init__(
        self, *, health: int = 0, attack: int = 0, energy: int = 0, room: Room
    ) -> None:
        super().__init__(health=health, attack=attack, energy=energy)
        self.room = room
        self.room.add_entity(self)
