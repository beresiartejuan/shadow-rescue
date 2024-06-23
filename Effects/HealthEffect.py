from Effects.Effect import Effect
from Entities.Entity import Entity


class HealthEffect(Effect):

    def __init__(self, *, name: str = "Healt Effect", uses: int = 1, health: int):
        super().__init__(name=name, uses=uses)
        self.health = health

    def use(self, entity: Entity):
        if self.uses > 0:
            entity.health += self.health
            self.uses -= 1
