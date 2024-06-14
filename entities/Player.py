from .EntityWithItems import EntityWithItems
from helper import clear


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

        bar = f"[Health: {self.health}] [Energy: {self.energy}]"
        location = "[Location: Masmorra I]"
        items_str = ""

        for s_item in items:
            items_str += (
                "|"
                + (" " * 4)
                + "Items"
                + (" " * 6)
                + s_item
                + (" " * (78 - 4 - 6 - 5 - len(s_item)))
                + "|"
                + "\n"
            )
        else:
            items_str = items_str[0:-1]

        print("┌" + ("-" * 78) + "┐")
        print("|", end="")
        print(" " * 4, end="")
        print("Status" + (" " * 5), end="")
        print(bar, end="")
        print(" " * (80 - 2 - 4 - 6 - 5 - len(bar)), end="")
        print("|")
        print("|" + (" " * 15) + location + (" " * (78 - 15 - len(location))) + "|")
        print("|" + (" " * 78) + "|")
        print(items_str)
        print("└" + ("-" * 78) + "┘")

    def showItemMenu(self):
        try:
            print("| ¿Deseas usar algún item?")
            options = enumerate(self.items)
            for key, item in options:
                print("|" + " " * 2 + f"[{key}: {item.name}]")

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
