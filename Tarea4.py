import csv
import graphviz

def cargar_desde_csv(archivo):
    datos = []
    try:
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                fila = []
                for item in row:
                    try:
                        num = int(item)
                        fila.append(str(num))  # Convertir números a strings para mantener el formato
                    except ValueError:
                        pass  # Omitir elementos que no son números
                if fila:
                    datos.append(fila)
        return datos
    except FileNotFoundError:
        print("El archivo especificado no existe.")
        return []

def ingresar_manualmente(datos):
    print("Ingrese los datos línea por línea. Presione Enter sin ingresar nada para terminar.")
    while True:
        entrada = input("Ingrese una línea de datos: ")
        if entrada:
            datos.append(entrada.split(','))
        else:
            break

def visualizar_datos(datos):
    if not datos:
        print("No hay datos para mostrar.")
    else:
        print("Datos:")
        for fila in datos:
            print(fila)

def generar_grafico_matriz(datos):
    if not datos:
        print("No hay datos para generar el gráfico.")
        return
    
    dot = graphviz.Digraph()
    num_filas = len(datos)
    num_columnas = len(datos[0])
    
    for fila in range(num_filas):
        for columna in range(num_columnas):
            valor = datos[fila][columna]
            if valor.strip() != "":
                dot.node(f"{fila}-{columna}", valor)
                if fila > 0:
                    dot.edge(f"{fila-1}-{columna}", f"{fila}-{columna}")
                if columna > 0:
                    dot.edge(f"{fila}-{columna-1}", f"{fila}-{columna}")
    
    dot.render('matriz_dispersa', format='png', cleanup=True)
    print("Se ha generado el gráfico de la matriz dispersa.")

def main():
    print("Bienvenido al programa de gestión de datos.")
    datos = []  # Inicializamos la matriz de datos vacía
    while True:
        print("\nOpciones:")
        print("1. Cargar desde un archivo CSV")
        print("2. Agregar datos manualmente")
        print("3. Visualizar datos")
        print("4. Generar gráfico de matriz dispersa")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            archivo = "D:\Archivos Mios Propios\Programacion\Phyton\DE LA U\heart_failure_clinical_records_dataset.csv"
            nuevos_datos = cargar_desde_csv(archivo)
            datos.extend(nuevos_datos)  # Agregar los nuevos datos al final de la matriz existente
        elif opcion == '2':
            ingresar_manualmente(datos)
        elif opcion == '3':
            visualizar_datos(datos)
        elif opcion == '4':
            generar_grafico_matriz(datos)
        elif opcion == '5':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
