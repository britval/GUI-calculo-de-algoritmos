# funciones.py

import DDA_izq as DDAI
import DDA_der as DDAD
import Bresenham as Bre
import Circunferencia as Cir
import Ellipse as Eli


def dda(x1, y1, x2, y2, direccion):
    print(f"Función DDA con los siguientes datos: x1={x1}, y1={y1}, x2={x2}, y2={y2}, dirección={direccion}")
    if direccion == "izquierda":
        Table= DDAI.generar_tabla(x1, y1, x2, y2)
        print("(x, y)")
        for punto in Table:
            print(punto[:2])
        return DDAI.graficar_tabla(Table)
    else:
        Table= DDAD.generar_tabla(x1, y1, x2, y2)
        print("(x, y)")
        for punto in Table:
            print(punto[:2])
        return DDAD.graficar_tabla(Table)

def bresenham(x1, y1, x2, y2, direccion=None):
    print(f"Función Bresenham con los siguientes datos: x1={x1}, y1={y1}, x2={x2}, y2={y2}")
    Table= Bre.generar_tabla(x1, y1, x2, y2)
    print("(x, y)")
    for punto in Table:
        print(punto[:2])
    return Bre.graficar_tabla(Table)

def circunferencia(Xc, Yc, R, direccion=None):
    print(f"Función Circunferencia con los siguientes datos: Xc={Xc}, Yc={Yc}, R={R}")
    Table= Cir.generar_tabla(Xc, Yc, R)
    print("(x, y)")
    for punto in Table:
        print(punto[:2])
    return Cir.graficar_tabla(Table)

def ellipse(Rx, Ry, Xc, Yc, direccion=None):
    print(f"Función Ellipse con los siguientes datos: Rx={Rx}, Ry={Ry}, Xc={Xc}, Yc={Yc}")
    segment1, segment2 = Eli.midptellipse(Rx, Ry)
    print("Segmento 1:")
    print("(x, y)")
    for punto in segment1:
        print(punto[:2])
    print("\nSegmento 2:")
    print("(x, y)")
    for punto in segment2:
        print(punto[:2])
    return Eli.plot_ellipse(segment1, segment2, center=(Xc, Yc))

# dda(5, 10, 10, 15, "Izquierda")
# bresenham(4, 3, 10, 8)
# circunferencia(1, 1, 5)
# ellipse(7, 11, -2, 3)