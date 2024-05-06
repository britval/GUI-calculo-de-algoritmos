import matplotlib.pyplot as plt

def generar_tabla(x1, y1, x2, y2):
    # Función para calcular delta x
    def dx(x1, x2):
        return x2 - x1

    # Función para calcular delta y
    def dy(y1, y2):
        return y2 - y1

    # Función para calcular p
    def p(dy, dx):
        return 2 * dy - dx

    # Función para calcular la pendiente
    def m(dx, dy):
        return dy / dx if dx != 0 else None

    # Inicializar tabla
    tabla = []

    # Ingresar x0, y0 y p0 como primer punto
    delta_x = dx(x1, x2)
    delta_y = dy(y1, y2)
    pendiente = m(delta_x, delta_y)
    pk = p(delta_y, delta_x)
    tabla.append((x1, y1, pk))

    # Evaluar pk
    x_actual, y_actual = x1, y1
    while x_actual < x2:
        if pk < 0:
            x_actual += 1
            pk += 2 * delta_y
        else:
            x_actual += 1
            y_actual += 1
            pk += 2 * delta_y - 2 * delta_x
        tabla.append((x_actual, y_actual, pk))

    return tabla



def graficar_tabla(tabla):
    # Extraer coordenadas x y y de la tabla
    coordenadas_x = [punto[0] for punto in tabla]
    coordenadas_y = [punto[1] for punto in tabla]

    # Graficar los puntos
    plt.plot(coordenadas_x, coordenadas_y, marker='o', linestyle='-')
    plt.title('Gráfico de Puntos Generados')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.show()

# Ejemplo de uso de las funciones
# if __name__ == "__main__":
#     x1, y1 = 4, 3
#     x2, y2 = 10, 8
#     tabla, pendiente, delta_x, delta_y = generar_tabla(x0, y0, x1, y1)
#     print("Pendiente:", pendiente) 
#     print("Delta x:", delta_x)
#     print("Delta y:", delta_y)
#     print("Tabla:")
#     for punto in tabla:
#         print(punto)
#     graficar_tabla(tabla)
