from .EntityWithItems import EntityWithItems
from helper import clear, s, c


class Player(EntityWithItems):

    def __init__(
        self, *, health: int = 100, attack: int = 10, energy: int = 15
    ) -> None:
        super().__init__(health=health, attack=attack, energy=energy)

    def showStatusBar(self):
        items = [
            "[Espacio Vacio]" if len(self.items) - 1 < i else self.items[i].__str__()
            for i in range(4)
        ]

        items_str = ""

        for s_item in items:
            specific_space = s(63 - len(s_item))
            items_str += f"|{s(4)}Items{s(6) + s_item + specific_space}|"
            items_str += "\n"
        else:
            items_str = items_str[0:-1]

        bar = f"[Health: {self.health}] [Energy: {self.energy}]"
        location = "[Location: Masmorra I]"

        print("┌" + c("-", 78) + "┐")
        print("|" + s(4) + "Status" + s(5) + bar + s(63 - len(bar)) + "|")
        print("|" + s(15) + location + s(78 - 15 - len(location)) + "|")
        print("|" + s(78) + "|")
        print(items_str)
        print("└" + c("-", 78) + "┘")

    def showItemMenu(self):
        try:
            print("| ¿Deseas usar algún item?")
            options = enumerate(self.items)
            for key, item in options:
                print("|" + s(2) + f"[{key}: {item.name}]")

            print("|  [Cualquier otra tecla para no usar ninguno]")
            print("|")
            user_choice = input("| ▸ ")

            index = int(user_choice)

            self.items[index].use(self)

            print(f"|  ¡Utilizaste [{self.items[index].name}]!")

            if self.items[index].uses == 0:
                del self.items[index]
        except:
            print(f"|  ¡Utilizaste [Nada]!")
            return
