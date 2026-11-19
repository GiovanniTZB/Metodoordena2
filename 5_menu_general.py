"""
Menú general: pide la cantidad de números y los números, luego los ordena
con el método elegido (ShellSort, Quicksort, Heapsort o Radix).
Repite hasta que el usuario elija salir.
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


def quick_sort(lista):
    """Divide y vencerás: elige un pivote y separa menores, iguales y mayores."""
    if len(lista) <= 1:
        return lista[:]
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


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


def _counting_por_digito(datos, exp):
    """Ordena de forma estable por el dígito que indica exp (1, 10, 100...)."""
    salida = [0] * len(datos)
    conteo = [0] * 10
    for x in datos:
        conteo[(x // exp) % 10] += 1
    for d in range(1, 10):
        conteo[d] += conteo[d - 1]
    for x in reversed(datos):
        d = (x // exp) % 10
        conteo[d] -= 1
        salida[conteo[d]] = x
    return salida


def _radix_positivos(datos):
    if not datos:
        return []
    exp = 1
    maximo = max(datos)
    while maximo // exp > 0:
        datos = _counting_por_digito(datos, exp)
        exp *= 10
    return datos


def radix_sort(lista):
    """Radix LSD: ordena dígito por dígito. Soporta negativos separándolos."""
    negativos = [-x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]
    neg_ord = [-x for x in reversed(_radix_positivos(negativos))]
    return neg_ord + _radix_positivos(positivos)


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


METODOS = {
    "1": ("ShellSort", shell_sort),
    "2": ("Quicksort", quick_sort),
    "3": ("Heapsort", heap_sort),
    "4": ("Radix", radix_sort),
}


def main():
    while True:
        print("\n===== MÉTODOS DE ORDENAMIENTO =====")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion in METODOS:
            nombre, funcion = METODOS[opcion]
            numeros = capturar_numeros()
            print("Original:", numeros)
            print(f"Ordenado con {nombre}:", funcion(numeros))
        elif opcion == "5":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
