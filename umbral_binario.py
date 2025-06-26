import cv2

# Leer la imagen original
imagen_color = cv2.imread('gato1.jpg')
if imagen_color is None:
    print("Imagen no encontrada.")
    exit()

# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Aplicar umbral binario
umbral = 127  # ← Puedes ajustar este valor entre 0 y 255
_, imagen_binaria = cv2.threshold(imagen_gris, umbral, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes 
cv2.imshow('Escala de grises', imagen_gris)
cv2.imshow('Umbral binario', imagen_binaria)

# Guardar resultado
cv2.imwrite('imagen_umbral_binario.jpg', imagen_binaria)

print("Imagen binaria guardada como 'imagen_umbral_binario.jpg'")
print("Presiona cualquier tecla para cerrar...")

cv2.waitKey(0)
cv2.destroyAllWindows()