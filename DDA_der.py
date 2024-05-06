import matplotlib.pyplot as plt

def generar_tabla(x1, y1, x2, y2):
    # Función para calcular el cambio en x
    def dx(x1, x2):
        return x2 - x1

    # Función para calcular el cambio en y
    def dy(y1, y2):
        return y2 - y1

    # Función para calcular la pendiente
    def m(dx, dy):
        return dy / dx if dx != 0 else None  # Manejar la división por cero

    # Inicializamos la tabla
    tabla = []

    # Ingresamos x1 y y1 como primeros datos de la tabla
    tabla.append((x1, y1))

    # Evaluar pendiente
    x_actual, y_actual = x1, y1
    while x_actual > x2:
        delta_x = dx(x1, x2)
        delta_y = dy(y1, y2)
        pendiente = m(delta_x, delta_y)
        
        if pendiente is not None:
            if (pendiente) <= 1:
                x_actual -= 1
                y_actual -= pendiente
            else:
                x_actual -= 1 / pendiente
                y_actual -= 1
            tabla.append((round(x_actual), round(y_actual)))

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
#     x1, y1 = -1, -1
#     x2, y2 = -8, -8
#     tabla = generar_tabla(x1, y1, x2, y2)
#     print("Tabla:")
#     for punto in tabla:
#         print(punto)
#     graficar_tabla(tabla)
