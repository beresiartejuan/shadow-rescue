from Entity import Entity


class Effect:

    def __init__(self, *, name: str, uses: int = 0):
        self.uses = uses
        self.name = name

    def use(self, entity: Entity) -> None: ...


class HealthEffect(Effect):

    def __init__(self, *, name: str = "Healt Effect", uses: int = 1, health: int):
        super().__init__(name=name, uses=uses)
        self.health = health

    def use(self, entity: Entity):
        if self.uses > 0:
            entity.health += self.health
            self.uses -= 1
