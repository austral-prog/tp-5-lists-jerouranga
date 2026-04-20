# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    matriz = lista_de_listas
    lista1 = matriz[0]
    lista2 = matriz[1]
    lista3 = matriz[2]
    del lista1[-1:1:-1]
    matriz[1] = lista2[1:4]
    del lista3[0:-2]

    return matriz



