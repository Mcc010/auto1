import string


reseñas = []

while True:
    reseña = input("Ingrese la reseña del producto (o '0' para terminar): ").lower()
    
    # Verificar salida y mínimo de 3 reseñas
    if reseña == "0":
        if len(reseñas) < 3:
            print("Debe ingresar al menos 3 reseñas antes de salir.")
            continue
        else:
            break
    
    # Eliminar signos de puntuación básicos
    reseña = reseña.translate(str.maketrans('', '', '.,!?'))
    
    
    reseñas.append(reseña)

#  Crear diccionario de frecuencias
diccionarioreseñas = {}
for reseña in reseñas:
    palabras = reseña.split()  # Separar en palabras
    for palabra in palabras:
        if palabra in diccionarioreseñas:
            diccionarioreseñas[palabra] += 1
        else:
            diccionarioreseñas[palabra] = 1

# Mostrar diccionario completo

print(diccionarioreseñas)

# Paso 5: Mostrar las 3 palabras más frecuentes
palabras_ordenadas = sorted(diccionarioreseñas.items(), key=lambda x: x[1], reverse=True)
print("\nLas 3 palabras más frecuentes son:")
for i in range(min(3, len(palabras_ordenadas))):
    palabra, frecuencia = palabras_ordenadas[i]
    print(f"{palabra}: {frecuencia}")