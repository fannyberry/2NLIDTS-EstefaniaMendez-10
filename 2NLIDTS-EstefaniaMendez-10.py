class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def _init_(self):
        self.cabeza = None  # Apuntador al primer nodo
        self.cola = None    # Apuntador al ultimo nodo


# Devuelve la "direccion" del nodo (0 si es None, como nullptr en C++)
def direccion(nodo):
    if nodo is None:
        return 0
    return id(nodo)


# Recorre la lista desde la cabeza hacia la cola
def imprimir_lista(lista):
    actual = lista.cabeza
    while actual is not None:
        print("Dato:", actual.dato,
              "| Direccion:", direccion(actual),
              "| Anterior:", direccion(actual.anterior),
              "| Siguiente:", direccion(actual.siguiente))
        actual = actual.siguiente
    print()


# Recorre la lista desde la cola hacia la cabeza (usando el apuntador anterior)
def imprimir_lista_reversa(lista):
    actual = lista.cola
    while actual is not None:
        print("Dato:", actual.dato,
              "| Direccion:", direccion(actual),
              "| Anterior:", direccion(actual.anterior),
              "| Siguiente:", direccion(actual.siguiente))
        actual = actual.anterior
    print()


def borrar_lista(lista):
    contador = 0
    while lista.cabeza is not None:
        siguiente = lista.cabeza.siguiente
        contador += 1
        print("Elemento borrado", contador,
              "| Dato:", lista.cabeza.dato,
              "| Direccion:", direccion(lista.cabeza))
        lista.cabeza = siguiente
    print("Total de elementos borrados:", contador)
    lista.cola = None


# Agrega un nodo al final; mantener la cola evita recorrer toda la lista
def agregar_nodo(lista, valor):
    nuevo_nodo = Nodo(valor)

    if lista.cabeza is None:
        # Lista vacia: el nuevo nodo es cabeza y cola a la vez
        lista.cabeza = nuevo_nodo
        lista.cola = nuevo_nodo
    else:
        lista.cola.siguiente = nuevo_nodo  # Último nodo apunta al nuevo
        nuevo_nodo.anterior = lista.cola   # Nuevo apunta de regreso al ultimo
        lista.cola = nuevo_nodo            # Nuevo pasa a ser la cola


def main():
    print("Actividad 08 - Lista Doblemente Enlazada")
    lista = ListaDoble()

    tamano_lista = int(input("Ingrese la cantidad de elementos de la lista enlazada: "))
    if tamano_lista <= 0:
        print("Cantidad de elementos no valida")
        return

    for i in range(tamano_lista):
        valor = int(input(f"Ingrese el dato {i + 1}: "))
        agregar_nodo(lista, valor)

    print("\nImprimiendo lista (de inicio a fin):")
    imprimir_lista(lista)

    print("Imprimiendo lista (de fin a inicio):")
    imprimir_lista_reversa(lista)

    print("\nBorrando lista de numeros")
    borrar_lista(lista)
    return 0

main()