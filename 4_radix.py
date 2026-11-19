"""
Ejercicio 4: Radix
Menú interactivo: pide la cantidad de números y los números, los ordena con
Radix y repite hasta que el usuario elija salir.
"""


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


def main():
    while True:
        print("\n===== Radix =====")
        print("1. Ordenar números con Radix")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            numeros = capturar_numeros()
            print("Original:", numeros)
            print("Ordenado:", radix_sort(numeros))
        elif opcion == "2":
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
