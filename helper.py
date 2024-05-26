import sys, os, time


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mecanografiar(texto: str, velocidad: float = 0.02):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        if (
            caracter.strip()
        ):  # Verificar si el caracter no es un espacio vacío o un salto de línea
            time.sleep(velocidad)
        else:
            time.sleep(0)
