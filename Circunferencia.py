import matplotlib.pyplot as plt

def generar_tabla(xc, yc, r):
    # Función para calcular P0
    def calcular_pk(r):
        calcular = 5/4 - r
        redondeo = round(calcular, 0)
        return redondeo

    # Inicializar tabla
    tabla = []

    # Calcular pk
    p = calcular_pk(r)

    # Insertar valores iniciales en la tabla
    tabla.append((0, r, p))

    # Calcular los puntos utilizando el algoritmo del punto medio de la circunferencia
    x = 0
    y = r
    while x <= y:
        if p < 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += 1 + (2 * x + 2) - (2 * y - 2)
        # Reflejar simétricamente los puntos en los otros siete octantes
        tabla.append((x, y, p))
        tabla.append((y, x, p))
        tabla.append((y, -x, p))
        tabla.append((x, -y, p))
        tabla.append((-x, -y, p))
        tabla.append((-y, -x, p))
        tabla.append((-y, x, p))
        tabla.append((-x, y, p))

    return tabla

def graficar_tabla(tabla):
    # Extraer coordenadas x y y de la tabla
    coordenadas_x = [punto[0] for punto in tabla]
    coordenadas_y = [punto[1] for punto in tabla]

    # Graficar los puntos
    plt.plot(coordenadas_x, coordenadas_y, linestyle='', marker='o', label='Tabla Original')
    plt.title('Circunferencia')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()  # Agregar leyenda
    plt.axis('equal')  # Para asegurar que los ejes X e Y tengan la misma escala
    plt.grid(True)
    plt.show()

# Ejemplo de uso de las funciones
# if __name__ == "__main__":
#     xc, yc = 1, 1
#     r = 5
#     tabla = generar_tabla_circunferencia(xc, yc, r)
#     print("Tabla:")
#     for punto in tabla:
#         print(punto)
#     graficar_tabla_circunferencia(tabla)
