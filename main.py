import random
import ipywidgets as widgets
from IPython.display import display, clear_output

# Configuración del tablero
ANCHO = 10
ALTO = 10

serpiente = [(5, 5)]
direccion = "DERECHA"
comida = (random.randint(0, 9), random.randint(0, 9))
puntos = 0

def mover():
    global serpiente

    cabeza_x, cabeza_y = serpiente[0]

    if direccion == "DERECHA":
        nueva = (cabeza_x + 1, cabeza_y)
    elif direccion == "IZQUIERDA":
        nueva = (cabeza_x - 1, cabeza_y)
    elif direccion == "ARRIBA":
        nueva = (cabeza_x, cabeza_y - 1)
    else:
        nueva = (cabeza_x, cabeza_y + 1)

    serpiente.insert(0, nueva)
    serpiente.pop()

def verificar_comida():
    global comida, puntos

    if serpiente[0] == comida:
        puntos += 1
        cola = serpiente[-1]
        serpiente.append(cola)
        comida = (
            random.randint(0, ANCHO - 1),
            random.randint(0, ALTO - 1)
        )

def verificar_colision():
    cabeza_x, cabeza_y = serpiente[0]

    if cabeza_x < 0 or cabeza_x >= ANCHO or cabeza_y < 0 or cabeza_y >= ALTO:
        print("GAME OVER")
        return True

    if serpiente[0] in serpiente[1:]:
        print("GAME OVER")
        return True

    return False

btn_arriba = widgets.Button(description="⬆️")
btn_abajo = widgets.Button(description="⬇️")
btn_izquierda = widgets.Button(description="⬅️")
btn_derecha = widgets.Button(description="➡️")

def dibujar():
    clear_output(wait=True)

    tablero = ""

    for y in range(ALTO):
        for x in range(ANCHO):
            if (x, y) == serpiente[0]:
                tablero += "🟢"
            elif (x, y) in serpiente:
                tablero += "🟩"
            elif (x, y) == comida:
                tablero += "🍎"
            else:
                tablero += "⬜"
        tablero += "\n"

    print(tablero)
    print("Puntos:", puntos)

    display(btn_arriba)
    display(btn_izquierda, btn_derecha)
    display(btn_abajo)

def arriba(b):
    global direccion
    direccion = "ARRIBA"
    mover()
    verificar_comida()
    dibujar()

def abajo(b):
    global direccion
    direccion = "ABAJO"
    mover()
    verificar_comida()
    dibujar()

def izquierda(b):
    global direccion
    direccion = "IZQUIERDA"
    mover()
    verificar_comida()
    dibujar()

def derecha(b):
    global direccion
    direccion = "DERECHA"
    mover()
    verificar_comida()
    dibujar()

btn_arriba.on_click(arriba)
btn_abajo.on_click(abajo)
btn_izquierda.on_click(izquierda)
btn_derecha.on_click(derecha)

dibujar()