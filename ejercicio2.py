import random

# Función para calcular el promedio
def calcular_promedio(lista):
    return sum(lista) / len(lista)

operadores = {
    "juan": "123",
    "maria": "456",
    "carlos": "789",
    "ana": "321",
    "luis": "654"
}

intentos = 0
acceso = False

# Login con máximo 5 intentos
while intentos < 5:
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario in operadores and operadores[usuario] == clave:
        acceso = True
        print("Acceso permitido")
        break
    else:
        print("Error")
        intentos += 1

# Si el acceso es correcto
if acceso:

    mediciones = []

    # Generar 50 rotaciones aleatorias
    for i in range(50):
        valor = random.randint(1, 120)
        mediciones.append(valor)

    print("mediciones generadas:", mediciones)

# Calcular promedio usando función
    promedio = calcular_promedio(mediciones)

    print("Promedio:", promedio)

    # Clasificación
    if promedio < 60:
        print("Operacion normal")
    elif promedio < 90:
        print("congestion severa")
    else:
        print("demora critica")