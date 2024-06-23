from Entities.MovableEntity import MovableEntity, Room
from helper import s, c, mecanografiar


class Player(MovableEntity):

    def __init__(self, room: Room) -> None:
        super().__init__(health=100, attack=10, energy=15, room=room)
        self.role = "player"

    def showStatusBar(self):
        items = [
            "[Espacio Vacio]" if len(self.items) - 1 < i else self.items[i].__str__()
            for i in range(4)
        ]

        items_str = ""

        for key, s_item in enumerate(items):
            specific_space = s(63 - len(s_item))
            items_str += f"|{s(4)}{'Items' if key == 0 else s(5)}{s(6) + s_item + specific_space}|"
            items_str += "\n"
        else:
            items_str = items_str[0:-1]

        bar = f"[Health: {self.health}] [Energy: {self.energy}]"
        location = f"[Location: {self.room.label}]"

        mecanografiar("┌" + c("-", 78) + "┐" + "\n", 1 / 40)
        mecanografiar(
            "|" + s(4) + "Status" + s(5) + bar + s(63 - len(bar)) + "|" + "\n", 1 / 40
        )
        mecanografiar(
            "|" + s(15) + location + s(78 - 15 - len(location)) + "|" + "\n", 1 / 40
        )
        mecanografiar("|" + s(78) + "|" + "\n", 1 / 40)
        mecanografiar(items_str + "\n", 1 / 40)
        mecanografiar("└" + c("-", 78) + "┘" + "\n", 1 / 40)

    def showItemMenu(self):
        try:
            mecanografiar("| ¿Deseas usar algún item?", 1 / 40)
            options = enumerate(self.items)
            for key, item in options:
                mecanografiar("|" + s(2) + f"[{key}: {item.name}]", 1 / 40)

            mecanografiar("|  [Cualquier otra tecla para no usar ninguno]", 1 / 40)
            mecanografiar("|", 1 / 40)
            user_choice = input("| ▸ ")

            index = int(user_choice)

            self.items[index].use(self)

            mecanografiar(f"|  ¡Utilizaste [{self.items[index].name}]!", 1 / 40)

            if self.items[index].uses == 0:
                del self.items[index]
        except:
            mecanografiar(f"|  ¡Utilizaste [Nada]!", 1 / 40)
            return
