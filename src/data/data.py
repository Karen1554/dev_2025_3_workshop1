class Data:
    def invertir_lista(self, lista):

        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def buscar_elemento(self, lista, elemento):

        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        vistos = set()  
        for elem in lista:
            clave = (elem, type(elem))
            if clave not in vistos:
                vistos.add(clave)
                resultado.append(elem)
        return resultado


    def merge_ordenado(self, lista1, lista2):

        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i]); i += 1
            else:
                resultado.append(lista2[j]); j += 1
        while i < len(lista1):
            resultado.append(lista1[i]); i += 1
        while j < len(lista2):
            resultado.append(lista2[j]); j += 1
        return resultado

    def rotar_lista(self, lista, k):

        if not lista:
            return []
        n = len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):

        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        return suma_esperada - sum(lista)

    def es_subconjunto(self, conjunto1, conjunto2):

        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True

    def implementar_pila(self):

        stack = []

        def push(item):
            stack.append(item)

        def pop():
            if not is_empty():
                return stack.pop()
            return None

        def peek():
            if not is_empty():
                return stack[-1]
            return None

        def is_empty():
            return len(stack) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty,
            "stack": stack,
        }

    def implementar_cola(self):

        cola = []

        def enqueue(item):
            cola.append(item)

        def dequeue():
            if not is_empty():
                return cola.pop(0)
            return None

        def peek():
            if not is_empty():
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty,
            "cola": cola,
        }

    def matriz_transpuesta(self, matriz):

        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        for fila in matriz:
            if len(fila) != columnas:
                raise ValueError("Todas las filas deben tener la misma longitud")
        return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
