#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:

superheroes = [
    "Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Ant-Man",
    "Wasp", "Scarlet Witch", "Vision", "Falcon", "Winter Soldier", "Capitan America"
]

#A
def buscaPersonaje(lista, buscado, index=0):
    """
        Busca de forma recursiva si un elemento está en una lista.

        Args:
            lista (list): La lista de elementos donde buscar.
            buscado (str): El elemento que se desea encontrar.
            index (int): Índice actual para recorrer la lista. Por defecto es 0.

        Funcionamiento:
            - Comienza desde el índice 0 y compara el elemento actual con el buscado.
            - Si encuentra el elemento, devuelve True.
            - Si llega al final de la lista sin encontrarlo, devuelve False.
            - Llama a sí misma incrementando el índice hasta que se cumpla una de las condiciones anteriores.
        """

    if index >= len(lista):
        return False
    if lista[index] == buscado:
        return True
    return buscaPersonaje(lista, buscado, index + 1)

#B
def listar(lista, index=0):
    """
    Recorre y muestra los elementos de una lista de forma recursiva.

    Args:
        lista (list): La lista de elementos a mostrar.
        index (int): Índice actual para recorrer la lista. Por defecto es 0.

    Funcionamiento:
        - Comienza desde el índice 0 y muestra el elemento actual.
        - Llama a sí misma incrementando el índice hasta que se hayan mostrado todos los elementos.
        - Finaliza cuando el índice supera la longitud de la lista.
    """

    if index >= len(lista):
        return
    print(lista[index])
    listar(lista, index + 1)

#Comprueba si el personaje ingresado existe y devuelve el mensaje.
resultado = buscaPersonaje(superheroes, "Capitan America")
if resultado:    
    print("Capitán América está en la lista")
else:
    print("El personaje no está en la lista.")

print()
print("-------------------------")
print()

print("Lista de superhéroes:")
print()
listar(superheroes)