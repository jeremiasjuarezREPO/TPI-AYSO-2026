def solicitar_primer_entero():
    while True:
#Pide primer numero al usuario
        entrada = input("Ingresa el primer número entero: ")
        try:
            return int(entrada)
        except ValueError:
            print("❌ Error: ¡Eso no es un número entero válido! Inténtalo de nuevo.")

#Pide segundo numero al usuario
def solicitar_segundo_entero():
    while True:
        entrada = input("Ingresa el segundo número entero: ")
        try:
            return int(entrada)
        except ValueError:
            print("❌ Error: ¡Eso no es un número entero válido! Inténtalo de nuevo.")

#Pide tercer numero al usuario
def solicitar_tercer_entero():
    while True:
        entrada = input("Ingresa el tercer número entero: ")
        try:
            return int(entrada)
        except ValueError:
            print("❌ Error: ¡Eso no es un número entero válido! Inténtalo de nuevo.")


print("--- Bienvenido al sistema de operaciones numéricas ---")

# Llamadas a las funciones
num1 = solicitar_primer_entero()
num2 = solicitar_segundo_entero()
num3 = solicitar_tercer_entero()

# Guardamos los números en una lista para las operaciones
numeros = [num1, num2, num3]

print("\n--- Resultados de las Operaciones ---")

# Suma
suma = sum(numeros)
print(f"🔹 Suma de los números: {suma}")

# Multiplicación
multiplicacion = num1 * num2 * num3
print(f"🔹 Multiplicación de los números: {multiplicacion}")

# Promedio
promedio = suma / len(numeros)
print(f"🔹 Promedio de los números: {promedio:.2f}")

# Orden de menor a mayor
numeros_ordenados = sorted(numeros)
print(f"🔹 Números ordenados de menor a mayor: {numeros_ordenados}")