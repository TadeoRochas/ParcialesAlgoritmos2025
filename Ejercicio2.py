from list__ import List
from super_heroes_data_ import superheroes
from Queue__ import Queue

class Personaje:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
            return f"Nombre: {self.name}\n Alias: {self.alias}\n Nombre real: {self.real_name}\n Bio: {self.short_bio}\n Año de aparición: {self.first_appearance}\n Tipo: {self.is_villain}"

listaPersonajes = List()

#carga los heroes de la lista importada en la listaPersonajes
for superhero in superheroes:
    hero = Personaje(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    listaPersonajes.append(hero)
#------------------------------------------------------------
#criterios usados
def criterioNombre(personaje):
    return personaje.name

listaPersonajes.add_criterion("nombre", criterioNombre)

def criterioAparicion(personaje):
    return personaje.first_appearance

listaPersonajes.add_criterion("first_appearance", criterioAparicion)

def criterioNombreReal(personaje):
    return str(personaje.real_name)

listaPersonajes.add_criterion("nombre_real", criterioNombreReal)
#------------------------------------------------------------
def buscarPosPorNombre(nombre):
    """
    Busca la posición de un personaje en la lista ordenada por nombre.

    Args:
        nombre (str): Nombre del personaje a buscar.

    Funcionamiento:
        - Ordena la lista `listaPersonajes` utilizando el criterio "nombre".
        - Utiliza el método `search` para encontrar la posición del personaje en la lista.
        - Si el personaje se encuentra, imprime su posición.
        - Si no se encuentra, imprime un mensaje indicando que no está en la lista.
    """
    pos = listaPersonajes.search(nombre, "nombre")
    if pos:
        print(f"{nombre} está en la posicion {pos}")
    else:
         print("El personaje no se encuentra en la lista.")

def listarVillanos():
    """
    Lista todos los personajes que son villanos.

    Funcionamiento:
        - Recorre la lista `listaPersonajes`.
        - Verifica si el atributo `is_villain` del personaje es True.
        - Imprime los datos del personaje si es un villano.
    """
    for personaje in listaPersonajes:
        if personaje.is_villain:
            print(personaje)

def listarVillanosAntesDe1980():
    """
    Lista todos los villanos que aparecieron antes de 1980.

    Funcionamiento:
        - Agrega todos los villanos a una cola.
        - Recorre la cola y verifica si el año de aparición del villano es anterior a 1980.
        - Imprime los datos de los villanos que cumplen con la condición.
    """

    listaPersonajes.sort_by_criterion("first_appearance")
    colaVillanos = Queue()

    for personaje in listaPersonajes:
        if personaje.is_villain:
            colaVillanos.arrive(personaje)

    print("Los villanos que aparecieron antes de 1980 son:")
    while not colaVillanos.qEmpty():
        villano = colaVillanos.attention()
        if villano.first_appearance < 1980:
            print(villano)

def listarSegunIniciales():
    """
    Lista los superhéroes cuyos nombres comienzan con las iniciales dadas, ordenados alfabéticamente.

    Funcionamiento:
        - Ordena la lista `listaPersonajes` por el atributo `name`.
        - Recorre la lista y verifica si el nombre del personaje comienza con alguna de las iniciales dadas.
        - Imprime los datos de los superhéroes que cumplen con la condición.
    """

    iniciales = ('Bl','G','My','W')

    listaPersonajes.sort_by_criterion("nombre")

    print("Los Superheroes que comienzan con las letras 'Bl', 'G', 'My' y 'W' son:")
    for superheroe in listaPersonajes:
        if superheroe.name.startswith(iniciales):
            print(superheroe)

def listadoNombreReal():
    """
    Lista los personajes ordenados por su nombre real de manera ascendente.

    Funcionamiento:
        - Ordena la lista `listaPersonajes` por el atributo `nombre_real`.
        - Recorre la lista y muestra los datos de cada personaje.
    """
    
    listaPersonajes.sort_by_criterion("nombre_real")

    print("Listado de personajes ordenado por nombre real de manera ascendente:")
    for personaje in listaPersonajes:
        print(personaje)

def listarFechaAparicion():
    """
    Lista los personajes ordenados por su año de aparición de manera ascendente.

    Funcionamiento:
        - Ordena la lista `listaPersonajes` utilizando el criterio "first_appearance".
        - Recorre la lista y muestra los datos de cada personaje en el orden establecido.
    """
    listaPersonajes.sort_by_criterion("first_appearance")

    print("Listado de personajes ordenado por año de aparición de manera ascendente:")
    for personaje in listaPersonajes:
        print(personaje)

def modificarNombreRealAntMan():
    """
    Modifica el nombre real del personaje 'Ant Man' a 'Scott Lang'.

    Funcionamiento:
        - Recorre la lista `listaPersonajes`.
        - Busca el personaje cuyo atributo `name` sea igual a 'Ant Man'.
        - Si lo encuentra, modifica su atributo `real_name` a 'Scott Lang' y muestra un mensaje indicando el cambio.
        - Si no lo encuentra, imprime un mensaje indicando que 'Ant Man' no está en la lista.
    """
    for personaje in listaPersonajes:
        if personaje.name == "Ant Man":
            personaje.real_name = "Scott Lang"
            print(f"El nombre real de {personaje.name} ha sido modificado a {personaje.real_name}.")
            return
    print("Ant-Man no se encuentra en la lista.")

def mostrarPorPalabraClave():
    """
    Muestra los personajes cuya biografía incluye las palabras 'time-traveling' o 'suit'.

    Funcionamiento:
        - Recorre la lista `listaPersonajes`.
        - Verifica si la biografía del personaje contiene las palabras clave.
        - Imprime los datos de los personajes que cumplen con la condición.
    """

    palabrasClave = ["time-traveling", "suit"]

    print("Personajes donde en su bibliografía se incluyen las palabras clave 'time-traveling' o 'suit':")
    for personaje in listaPersonajes:
        for palabra in palabrasClave:
            if palabra in personaje.short_bio.lower():
                print(personaje)
                break

def eliminarBuscado(buscado):
    for personaje in listaPersonajes:
        if personaje.name == buscado:
            listaPersonajes.remove(personaje)
            print(f"Se eliminó el personaje:\n{personaje}")
            return
    print(f"{buscado} no se encuentra en la lista.")
            
print()
print("-------------------------")
print()

#La lista se muestra muchas veces para comodidad mía ir controlando que todo se cumpla, le sugiero comentar para ver mejor.


#Listado ordenado de manera ascendente por nombre de los personajes.
listaPersonajes.sort_by_criterion("nombre")
listaPersonajes.show()

print()
print("-------------------------")
print()

#Determinar en que posicion esta The Thing y Rocket Raccoon.
#--------
#aclaración:
#Si la posición debe ser en la lista sin ordenar, osea en la original, esto se puede mover antes de que se ordene por nombre.
#Está así por orden de los ejercicios
buscarPosPorNombre("The Thing")
buscarPosPorNombre("Rocket Raccoon")

print()
print("-------------------------")
print()

#Listar todos los villanos de la lista.
listarVillanos()

print()
print("-------------------------")
print()

# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
listarVillanosAntesDe1980()

print()
print("-------------------------")
print()

#Listar los superheores que comienzan con  Bl, G, My, y W.
listarSegunIniciales()

print()
print("-------------------------")
print()

#Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
listadoNombreReal()

print()
print("-------------------------")
print()

# Listado de superheroes ordenados por fecha de aparación.
listarFechaAparicion()

print()
print("-------------------------")
print()

# Modificar el nombre real de Ant Man a Scott Lang.
modificarNombreRealAntMan()

print()
print("-------------------------")
print()

#Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
mostrarPorPalabraClave()

print()
print("-------------------------")
print()

#Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista
eliminarBuscado("Electro")
eliminarBuscado("Baron Zemo")
