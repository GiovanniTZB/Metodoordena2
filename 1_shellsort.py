"""
Ejercicio 1: ShellSort
Menú interactivo: pide la cantidad de números y los números, los ordena con
ShellSort y repite hasta que el usuario elija salir.
"""


def shell_sort(lista):
    """Inserción con saltos (gap) que se reducen a la mitad hasta llegar a 1."""
    datos = lista[:]
    n = len(datos)
    salto = n // 2
    while salto > 0:
        for i in range(salto, n):
            temp = datos[i]
            j = i
            while j >= salto and datos[j - salto] > temp:
                datos[j] = datos[j - salto]
                j -= salto
            datos[j] = temp
        salto //= 2
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
        print("\n===== ShellSort =====")
        print("1. Ordenar números con ShellSort")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            numeros = capturar_numeros()
            print("Original:", numeros)
            print("Ordenado:", shell_sort(numeros))
        elif opcion == "2":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
