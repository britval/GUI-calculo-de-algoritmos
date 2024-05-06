import matplotlib.pyplot as plt

def midptellipse(rx, ry, xc=0, yc=0):
    x = 0
    y = ry
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    # Listas para almacenar los puntos de los segmentos 1 y 2
    segment1_points = []
    segment2_points = []

    while (dx < dy):
        # Almacenar puntos del segmento 1
        segment1_points.append((x + xc, y + yc))
        segment1_points.append((-x + xc, y + yc))
        segment1_points.append((x + xc, -y + yc))
        segment1_points.append((-x + xc, -y + yc))

        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
           (rx * rx * ry * ry))

    while (y >= 0):
        # Almacenar puntos del segmento 2
        segment2_points.append((x + xc, y + yc))
        segment2_points.append((-x + xc, y + yc))
        segment2_points.append((x + xc, -y + yc))
        segment2_points.append((-x + xc, -y + yc))

        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

    return segment1_points, segment2_points

def plot_ellipse(segment1_points, segment2_points, center=(0, 0)):
    # Obtener las coordenadas x e y de los puntos del segmento 1 y 2
    segment1_x = [point[0] + center[0] for point in segment1_points]
    segment1_y = [point[1] + center[1] for point in segment1_points]
    segment2_x = [point[0] + center[0] for point in segment2_points]
    segment2_y = [point[1] + center[1] for point in segment2_points]

    # Dibujar la elipse
    plt.plot(segment1_x, segment1_y, 'bo')
    plt.plot(segment2_x, segment2_y, 'ro')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Mid-Point Ellipse Drawing Algorithm')
    plt.grid(True)
    plt.show()

# Ejemplo de uso de las funciones
# if __name__ == "__main__":
#     rx, ry = -7, 11
#     segment1, segment2 = midptellipse(rx, ry)
#     print("Segmento 1:")
#     print(segment1)
#     print("\nSegmento 2:")
#     print(segment2)
#     # Centro de la elipse
#     center = (-2, 3)
#     # Graficar la elipse con centro personalizado
#     plot_ellipse(segment1, segment2, center)
