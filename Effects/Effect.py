from Entities.Entity import Entity
from abc import ABC, abstractmethod


class Effect(ABC):

    def __init__(self, *, name: str, uses: int = 0):
        self.uses = uses
        self.name = name

    @abstractmethod
    def use(self, entity: Entity) -> None:
        pass
