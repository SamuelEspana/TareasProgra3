import os
import graphviz

class nodoArbol:
    def __init__(self, Valor):
        self.izq = None
        self.der = None
        self.valor = Valor

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self.insertar2(valor, self.raiz)

    def insertar2(self, valor, nodo):
        if nodo is None:
            return nodoArbol(valor)
        if valor < nodo.valor:
            nodo.izq = self.insertar2(valor, nodo.izq)
        elif valor > nodo.valor:
            nodo.der = self.insertar2(valor, nodo.der)
        return nodo
    
    def mostrar(self, nodo):
        if nodo is not None:
            if nodo.izq is not None:
                print(nodo.valor, "->", nodo.izq.valor)
            if nodo.der is not None:
                print(nodo.valor, "->", nodo.der.valor)
            self.mostrar(nodo.izq)
            self.mostrar(nodo.der)

    def CargarArchivo(self):
        archivo = input("\nPor favor, arrastre su archivo o digite su ruta: ").strip("\"' &")
        if not os.path.isfile(archivo):
            print("El archivo no existe.")
        else:
            with open(archivo, 'r') as file:
                for linea in file:
                    arbol.insertar(int(linea.strip()))
            print("\nInsercion de los datos del archivo exitosa: ")
            arbol.mostrar(arbol.raiz)
            
    def buscar(self, valor, nodo, profundidad=0):
        if nodo is None or nodo.valor == valor:
            return nodo, nodo.valor if nodo else None, profundidad
        if valor < nodo.valor:
            return self.buscar(valor, nodo.izq, profundidad+1)
        return self.buscar(valor, nodo.der,profundidad+1)

    def buscar_nodo_profundidad(self, valor):
        nodo, valor_encontrado, profundidad = self.buscar(valor, self.raiz)
        return nodo, valor_encontrado, profundidad
    
    def eliminar(self, valor):
        self.raiz = self.eliminar_nodo(self.raiz, valor)

    def eliminar_nodo(self, nodo, valor):
        if nodo is None:
            return nodo
        # Busca el nodo a eliminar
        if valor < nodo.valor:
            nodo.izq = self.eliminar_nodo(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self.eliminar_nodo(nodo.der, valor)
        else:  # Encontr� el nodo a eliminar
            # Caso 1: Nodo es una hoja o tiene un solo hijo
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # Caso 2: Nodo tiene dos hijos
            # Encuentra el sucesor inmediato (el menor valor en el sub�rbol derecho)
            sucesor = self.min_valor_nodo(nodo.der)
            # Copia el valor del sucesor al nodo que se va a eliminar
            nodo.valor = sucesor.valor
            # Elimina el sucesor
            nodo.der = self.eliminar_nodo(nodo.der, sucesor.valor)
        return nodo

    def min_valor_nodo(self, nodo):
        actual = nodo
        # Recorre el �rbol hacia la izquierda para encontrar el nodo con el valor m�nimo
        while actual.izq is not None:
            actual = actual.izq
        return actual
    
    def graficar_arbol(self):
        dot = graphviz.Digraph()
        self._graficar_nodo(dot, self.raiz)
        dot.render('arbol', format='png', cleanup=True)
        os.system('arbol.png')

    def _graficar_nodo(self, dot, nodo):
        if nodo is not None:
            dot.node(str(nodo.valor))
        if nodo.izq is not None:
            dot.edge(str(nodo.valor), str(nodo.izq.valor))
            self._graficar_nodo(dot, nodo.izq)
        if nodo.der is not None:
            dot.edge(str(nodo.valor), str(nodo.der.valor))
            self._graficar_nodo(dot, nodo.der)



arbol = ABB()
opc = 0
while(opc != 5):
    print("\n-------Menu-------")
    print("1. Insertar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Cargar Archivo")
    print("5. Graficar Árbol")
    print("6. Salir")
    opc = int(input("Ingrese su opcion: "))
    if(opc==1):
      numero=int(input("Ingrese el valor a insertar en el arbol: "))
      arbol.insertar(numero)
      arbol.mostrar(arbol.raiz)
    elif(opc==2):
        numero = int(input("Ingrese el valor a buscar en el arbol: "))
        nodo_encontrado, valor_encontrado, profundidad = arbol.buscar_nodo_profundidad(numero)
        if nodo_encontrado:
            print(f"El valor {valor_encontrado} se encontro en el arbol en la profundidad {profundidad}.")
        else:
            print(f"El valor {numero} no se encontro en el arbol.")
    elif(opc==3):
        numero = int(input("Ingrese el valor a eliminar del arbol: "))
        arbol.eliminar(numero)
        arbol.mostrar(arbol.raiz)
    elif(opc == 4):
        arbol.CargarArchivo()
    elif(opc ==5):
        arbol.graficar_arbol()
    else:
        break;