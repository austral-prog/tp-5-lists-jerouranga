# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    longitud = len(lista)
    if longitud >= 6:
       del lista[0]
       del lista[3:5]
       return lista
    elif longitud == 5:
       del lista[0]
       del lista [3]
       return lista
    elif longitud < 5 and len(lista) > 0:
       del lista[0]
       return lista
    else:
       return lista
