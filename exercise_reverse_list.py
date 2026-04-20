# Ejercicio 8: Invertir una lista

def reverse_list(lista):
    """
    Retorna una nueva lista con los elementos en orden inverso.

    Args:
        lista: Una lista de elementos

    Returns:
        Una nueva lista con los elementos en orden inverso
    """
    original = lista[:]
    nueva = original[: : -1]
    return nueva

