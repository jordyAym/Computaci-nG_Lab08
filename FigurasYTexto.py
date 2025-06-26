import cv2

# Leer la imagen original
imagen = cv2.imread('perro.jpg')

if imagen is None:
    print("Imagen no encontrada. Asegúrate de tener 'gato.jpg' en la misma carpeta.")
    exit()

# Crear una copia para editar
imagen_dibujo = imagen.copy()

# Variables globales
coordenada_centro = None
radio = 100
texto = "Perro"

# Función que se ejecuta al hacer clic
def dibujar(event, x, y, flags, param):
    global coordenada_centro

    if event == cv2.EVENT_LBUTTONDOWN:
        coordenada_centro = (x, y)
        print(f"Círculo dibujado en: {coordenada_centro}")

        # Dibujar círculo
        cv2.circle(imagen_dibujo, coordenada_centro, radio, (0, 255, 0), 3)

        # Dibujar texto
        posicion_texto = (x - 40, y - 60)
        cv2.putText(imagen_dibujo, texto, posicion_texto, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Crear ventana y vincular función de clic
cv2.namedWindow('Haz clic para anotar')
cv2.setMouseCallback('Haz clic para anotar', dibujar)

print("Haz clic sobre la cara de la figura para dibujar un círculo y texto.")
print("Presiona 's' para guardar o 'q' para salir sin guardar.")

while True:
    cv2.imshow('Haz clic para anotar', imagen_dibujo)
    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord('q'):
        break
    elif tecla == ord('s'):
        cv2.imwrite('imagen_anotada.jpg', imagen_dibujo)
        print("Imagen guardada como 'imagen_anotada.jpg'")
        break

cv2.destroyAllWindows()

