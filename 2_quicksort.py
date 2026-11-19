"""
Ejercicio 2: Quicksort
Menú interactivo: pide la cantidad de números y los números, los ordena con
Quicksort y repite hasta que el usuario elija salir.
"""


def quick_sort(lista):
    """Divide y vencerás: elige un pivote y separa menores, iguales y mayores."""
    if len(lista) <= 1:
        return lista[:]
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


def pedir_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  Debe ser un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Entrada no válida, escribe un número entero.")


def capturar_numeros():
    cantidad = pedir_entero("¿Cuántos números quieres ordenar? ", 1)
    numeros = []
    for i in range(cantidad):
        numeros.append(pedir_entero(f"  Número {i + 1}: "))
    return numeros


def main():
    while True:
        print("\n===== Quicksort =====")
        print("1. Ordenar números con Quicksort")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            numeros = capturar_numeros()
            print("Original:", numeros)
            print("Ordenado:", quick_sort(numeros))
        elif opcion == "2":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
