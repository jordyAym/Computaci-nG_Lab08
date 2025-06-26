import cv2
import numpy as np

# Leer imagen
imagen = cv2.imread('img1.jpg')

if imagen is None:
    print("Imagen no encontrada. Asegúrate de tener 'img1.jpg' en la misma carpeta.")
    exit()

# Separar canales originales
B, G, R = cv2.split(imagen)

# Estado inicial de cada canal
mostrar_R = True
mostrar_G = True
mostrar_B = True

# Crear ventana solo una vez
cv2.namedWindow('Canales RGB Interactivo', cv2.WINDOW_AUTOSIZE)

print("Presiona 'r' (rojo), 'g' (verde), 'b' (azul). 'q' para salir.")

while True:
    # Construir los canales según los estados actuales
    canal_b = B if mostrar_B else np.zeros_like(B)
    canal_g = G if mostrar_G else np.zeros_like(G)
    canal_r = R if mostrar_R else np.zeros_like(R)

    # Combinar los canales activos
    imagen_mostrada = cv2.merge([canal_b, canal_g, canal_r])

    # Mostrar imagen
    cv2.imshow('Canales RGB Interactivo', imagen_mostrada)

    # Esperar 1 ms por una tecla
    tecla = cv2.waitKey(1) & 0xFF

    # Manejo de teclas
    if tecla == ord('q'):
        break
    elif tecla == ord('r'):
        mostrar_R = not mostrar_R
    elif tecla == ord('g'):
        mostrar_G = not mostrar_G
    elif tecla == ord('b'):
        mostrar_B = not mostrar_B

# Cerrar todas las ventanas al salir
cv2.destroyAllWindows()
