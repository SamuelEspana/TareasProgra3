import csv
import tkinter as tk
import os
from tkinter import filedialog
from flask import Flask, jsonify, request
app = Flask(__name__)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, callback=None):
        """
        Realiza un recorrido en orden (in-order traversal) del árbol
        e imprime los valores de los nodos en orden ascendente.
        """
        nodes = []  # Lista para almacenar los nodos
        def traverse(node):
            if node is not None:
                traverse(node.left)
                nodes.append(node.value)
                traverse(node.right)
        
        traverse(self.root)
        return nodes

    def search(self, value):
        """
        Busca un valor en el árbol binario.
        Retorna True si el valor está presente, False de lo contrario.
        """
        current = self.root
        parent = None
        while current is not None:
            if current.value == value:
                print("El valor está presente en el árbol.")
                if current.left:
                    print(f"Subárbol izquierdo de {current.value}: {current.left.value}")
                if current.right:
                    print(f"Subárbol derecho de {current.value}: {current.right.value}")
                return True
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        print("El valor no está presente en el árbol.")
        if parent:
            print(f"El valor debería estar en el subárbol {'izquierdo' if value < parent.value else 'derecho'} de {parent.value}.")
        return False


    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)



def insert_csv_to_binary_tree(csv_file_path):
    binary_tree = BinaryTree()

    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row:  
                value = row[0]  
                binary_tree.insert(value)
    return binary_tree


def main_menu():
    binary_tree = BinaryTree()  # Crear un árbol vacío al inicio
    while True:
        print("\nMenú Principal:")
        print("1. Cargar archivo CSV")
        print("2. Insertar de forma manual")
        print("3. Buscar registro")
        print("4. Mostrar arbol in-order")
        print("5. Salir")

        choice = input("Por favor, seleccione una opción: ")

        if choice == "1":
            binary_tree = insert_csv_to_binary_tree()
        elif choice == "2":
            value = input("Ingrese el valor que desea insertar: ")
            binary_tree.insert(value)
            print(f"El valor {value} ha sido insertado en el árbol.")
        elif choice == "3":
            if binary_tree is None:
                print("El árbol está vacío. Por favor, carga un archivo CSV primero o inserta valores manualmente.")
            else:
                value = input("Ingrese el valor que desea buscar: ")
                if binary_tree.search(value):
                    print("El valor está presente en el árbol.")
                else:
                    print("El valor no está presente en el árbol.")
        elif choice == "4":
            binary_tree.inorder_traversal()
        elif choice == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

binaryTree = BinaryTree()

port = int(os.environ.get('PORT', 5000))

@app.route('/add_nodo_manual', methods=['POST'])
def add_nodo_manual():
    data = request.json
    value = data.get('value')
    if not value :
        return jsonify({'error': 'Ingrese un valor'}), 400
    binaryTree.insert(value)
    return jsonify({'message': 'nodo registrado correctamente'}), 201

@app.route('/list_arbol', methods=['GET'])
def list_arbol():
    nodos = binaryTree.inorder_traversal()  # Usar la instancia de BinaryTree creada fuera de la función
    return jsonify({'nodos': nodos}), 200

@app.route('/search_arbol', methods=['GET'])
def search_arbol():
    value = request.args.get('value')  # Obtener el valor a buscar de los parámetros de la solicitud
    if not value:
        return jsonify({'error': 'Ingrese un valor para buscar'}), 400
    
    # Realizar la búsqueda en el árbol binario
    if binaryTree.search(value):
        return jsonify({'message': f'El valor {value} está presente en el árbol'}), 200
    else:
        return jsonify({'message': f'El valor {value} no está presente en el árbol'}), 404

@app.route('/integrantes', methods=['GET'])
def integrantes():
    nombres = ["Mario Culajay 9490-22-5771", "Jhonatan Rojelio 9490-22-4512", "Sergio Sanchez 9490-22-8463", "Samuel España 9490-22-8751"]
    return jsonify(nombres), 200

@app.route('/insertar_csv', methods=['POST'])
def insertar_csv():
    data = request.json
    csv_file_path = data.get('csv_file_path')
    if not os.path.exists(csv_file_path):
        return jsonify({'error': 'El archivo CSV no existe'}), 404
    
    binary_tree = insert_csv_to_binary_tree(csv_file_path)  # Llama a la función con la ruta del archivo CSV
    return jsonify({'message': 'Datos del archivo CSV insertados correctamente'}), 201


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'respuesta': 'done'}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
