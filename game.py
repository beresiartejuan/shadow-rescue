from helper import *
from Item import Item
from Player import Player
from Effect import HealthEffect

INIT_TEXT = """
┌---------------------------------------------------------------------------------┐
| El bosque siempre fue mi refugio, hasta hoy. Durante un paseo, mientras         |
| cortaba un árbol, los gruñidos de mi perro rasgaron la calma. Corrí hacia       |
| él y lo vi siendo arrastrado por lobos hacia una cueva oscura.                  |
|                                                                                 |
| A pesar de los años, mi espíritu sigue indomable. Con las herramientas de       |
| mi oficio y el fuego de mi determinación, me adentro en la cueva para rescatar  |
| a mi compañero. No hay miedo que me detenga, ni oscuridad que me disuada.       |
|                                                                                 |
| Hoy, el bosque es el escenario de una aventura no deseada, pero necesaria.      |
| Por mi amigo, enfrentaré lo que sea...                                          |
└---------------------------------------------------------------------------------┘

"""

skip_intro = True

player = Player()

hacha = Item(name="Hacha", attack=15, defense=1, uses=10)

pan = Item(name="Pan", attack=0, defense=0, uses=1)

pan.setEffect(HealthEffect(health=10))

player.add_item(hacha)
player.add_item(pan)

while True:

    clear()

    if not skip_intro:
        mecanografiar(INIT_TEXT)

    input("[Presiona ENTER para continuar...]")

    clear()

    player.showStatusBar()

    print("\n")

    player.showItemMenu()

    print("\n")

    player.showStatusBar()

    break
