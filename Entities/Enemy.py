from Entities.IdentifiableEntity import IdentifiableEntity


class Enemy(IdentifiableEntity):

    def __init__(self, *, health: int, attack: int, energy: int) -> None:
        super().__init__(health=health, attack=attack, energy=energy)
        self.role = "enemy"
