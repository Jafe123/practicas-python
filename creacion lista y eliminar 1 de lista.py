hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

hat_list[3]=111
print("monstrar nueva lista de hat: ",hat_list)# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
print("\nLongitud de la lista: ", len(hat_list))

del hat_list[1]  # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
print("Longitud de la nueva lista:", len(hat_list)) # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("\nNuevo contenido de la lista:", hat_list)
print(hat_list)

