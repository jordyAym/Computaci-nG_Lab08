import cv2
import numpy as np

# Crear un lienzo blanco
ancho, alto = 800, 600
lienzo = np.ones((alto, ancho, 3), dtype=np.uint8) * 255
historial = [lienzo.copy()]  # Para deshacer

# Variables de estado
dibujando = False
punto_inicio = (0, 0)
forma = 'rectangulo'  # rectangulo, circulo, linea

# Función para dibujar según la forma actual
def dibujar_forma(img, pt1, pt2, forma):
    if forma == 'rectangulo':
        cv2.rectangle(img, pt1, pt2, (0, 0, 255), 2)
    elif forma == 'circulo':
        radio = int(np.linalg.norm(np.array(pt2) - np.array(pt1)))
        cv2.circle(img, pt1, radio, (0, 255, 0), 2)
    elif forma == 'linea':
        cv2.line(img, pt1, pt2, (255, 0, 0), 2)

# Evento del mouse
def mouse_evento(event, x, y, flags, param):
    global dibujando, punto_inicio, lienzo, historial

    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        punto_inicio = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        punto_final = (x, y)
        dibujar_forma(lienzo, punto_inicio, punto_final, forma)
        historial.append(lienzo.copy())

# Ventana e interacción
cv2.namedWindow("Lienzo de dibujo")
cv2.setMouseCallback("Lienzo de dibujo", mouse_evento)

print("  Dibuja con el mouse. Usa teclas:")
print("  'r' = rectángulo | 'c' = círculo | 'l' = línea")
print("  'z' = deshacer    | 's' = guardar | 'q' = salir")

while True:
    cv2.imshow("Lienzo de dibujo", lienzo)
    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord('q'):
        break
    elif tecla == ord('r'):
        forma = 'rectangulo'
        print(" Modo: Rectángulo")
    elif tecla == ord('c'):
        forma = 'circulo'
        print(" Modo: Círculo")
    elif tecla == ord('l'):
        forma = 'linea'
        print(" Modo: Línea")
    elif tecla == ord('z'):
        if len(historial) > 1:
            historial.pop()
            lienzo = historial[-1].copy()
            print(" Deshacer")
        else:
            print(" Nada que deshacer")
    elif tecla == ord('s'):
        cv2.imwrite("dibujo_final.jpg", lienzo)
        print(" Imagen guardada como 'dibujo_final.jpg'")

cv2.destroyAllWindows()
