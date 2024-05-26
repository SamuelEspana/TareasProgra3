import csv
import os
from typing import Any, List, Tuple

class HashTable:
    def __init__(self, size: int = 100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key: Any) -> int:
        return hash(key) % self.size
    
    def insert(self, key: Any, value: Any):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Remplaza el valor si ya existe
                return
        bucket.append((key, value)) # Agregar el nuevo registro sino encontro coincidencias
    
    def search_by_key(self, key: Any) -> Any:
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def search_by_value(self, value: Any) -> List[Any]:
        result = []
        for bucket in self.table:
            for k, v in bucket:
                if v == value:
                    result.append(k)
        return result
    
    def load_from_csv(self, filepath: str):
        if not os.path.isfile(filepath):
            print(f"Error: El archivo '{filepath}' no existe.")
            return
        
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:  # ver que tenga por lo menso 2 columnas
                    key, value = row[0], row[1]   # tomar las primeras 2 columas para la clave y valor
                    self.insert(key, value)
                    print(f"Insertado desde CSV: clave = {key}, valor = {value}")
                else:
                    print(f"Fila con formato incorrecto (menos de 2 columnas): {row}")

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")

def main():
    hash_table = HashTable(size=10)
    
    while True:
        print("\nMenu:")
        print("1. Insertar manualmente datos")
        print("2. Buscar por clave")
        print("3. Buscar por valor")
        print("4. Cargar datos desde archivo CSV")
        print("5. Mostrar todos los registros")
        print("6. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == '1':
            key = input("Ingrese la clave: ")
            value = input("Ingrese el valor: ")
            hash_table.insert(key, value)
            print(f"Insertado: clave = {key}, valor = {value}, hash = {hash(key) % hash_table.size}")
        
        elif choice == '2':
            key = input("Ingrese la clave a buscar: ")
            result = hash_table.search_by_key(key)
            if result is not None:
                print(f"Valor encontrado para la clave {key}: {result}")
            else:
                print(f"No se encontró valor para la clave {key}.")
        
        elif choice == '3':
            value = input("Ingrese el valor a buscar: ")
            result = hash_table.search_by_value(value)
            if result:
                print(f"Claves encontradas para el valor {value}: {result}")
            else:
                print(f"No se encontraron claves para el valor {value}.")
        
        elif choice == '4':
            filepath = input("Ingrese la ruta del archivo CSV: ")
            hash_table.load_from_csv(filepath)
            print("Datos cargados desde el archivo CSV.")
        
        elif choice == '5':
            hash_table.display()
        
        elif choice == '6':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()