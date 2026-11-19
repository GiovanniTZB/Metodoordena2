"""
Ejercicio 3: Heapsort
Menú interactivo: pide la cantidad de números y los números, los ordena con
Heapsort y repite hasta que el usuario elija salir.
"""


def _heapify(datos, n, i):
    """Mantiene la propiedad de montículo máximo en el subárbol de la posición i."""
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2
    if izq < n and datos[izq] > datos[mayor]:
        mayor = izq
    if der < n and datos[der] > datos[mayor]:
        mayor = der
    if mayor != i:
        datos[i], datos[mayor] = datos[mayor], datos[i]
        _heapify(datos, n, mayor)


def heap_sort(lista):
    """Construye un montículo máximo y extrae el mayor repetidamente."""
    datos = lista[:]
    n = len(datos)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(datos, n, i)
    for fin in range(n - 1, 0, -1):
        datos[0], datos[fin] = datos[fin], datos[0]
        _heapify(datos, fin, 0)
    return datos


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
        print("\n===== Heapsort =====")
        print("1. Ordenar números con Heapsort")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            numeros = capturar_numeros()
            print("Original:", numeros)
            print("Ordenado:", heap_sort(numeros))
        elif opcion == "2":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
