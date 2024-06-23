from helper import *
from dialogs import *
from config import *
from Rooms.Rooms import Forest
from Entities.Player import Player

from Items.Axe import Axe
from Items.Bread import Bread

###################
#  ROOMS          #
###################

forest = Forest()
player = Player(forest)
player.add_item(Axe())
player.add_item(Bread())


clear()


def loop():
    global veces, player

    clear()

    player.showStatusBar()


if not SKIP_INTRO:
    mecanografiar(INIT_TEXT)
    input("[Presiona ENTER para continuar...]")
    clear()

while True:

    if not loop():
        break
