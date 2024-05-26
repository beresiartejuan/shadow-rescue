class Entity:

    def __init__(self, *, health: int = 0, attack: int = 0, energy: int = 0) -> None:
        self.health = health
        self.attack = attack
        self.energy = energy

    def get_damage(self, *, damage: int) -> int:
        self.healt -= damage
        return self.health