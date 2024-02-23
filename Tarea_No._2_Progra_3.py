def binario(decimal):
    if(decimal==0):
        return ""
    elif(decimal<0):
        return "Por favor ingrese un entero positivo"
    else:
        return binario(decimal//2)+str(decimal%2)

def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

def calcular_raiz_cuadrada(numero, aproximacion, bajo, alto):
    media = (alto + bajo) / 2
    aproximacion_cuadrado = media * media
    if abs(aproximacion_cuadrado - numero) <= aproximacion:
        return int(media)
    elif aproximacion_cuadrado > numero:
        return calcular_raiz_cuadrada(numero, aproximacion, bajo, media)
    else:
        return calcular_raiz_cuadrada(numero, aproximacion, media, alto)

def raiz_cuadrada_entera(numero):
    try:
        num = int(numero)
        if(numero < 0):
            print("El numero ingresado no puede ser negativo")
        else:
            return calcular_raiz_cuadrada(numero, 0.0001, 0, numero)
    except ValueError:
        print("Ingrese valores positivos")

def suma_numeros_enteros(num,contador=1):
    if num == 1:
        return 1
    elif contador <= num:
        contador =+1
        return num + suma_numeros_enteros(num-1)

def normal_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sistema = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numero_romano = ''
    i = 0
    while  numero > 0:
        for _ in range(numero // valores[i]):
            if (numero // valores[i]>0):
                numero_romano += sistema[i]
                numero = numero-valores[i]
            else:
                pass
        i += 1  
    return numero_romano

def main():
    while True:
        print("\nMenu:")
        print("1. Convertir entero a binario")
        print("2. Contar digitos de un entero")
        print("3. Raiz cuadrada entera")
        print("4. Convertir decimal a romano")
        print("5. Suma de numeros enteros")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            numero = input("Ingrese el numero que desea convertir a binario: ")
            try:
                numero = int(numero)
                print(binario(numero))
            except ValueError:
                print("Por favor, ingrese unicamente numeros enteros")
        elif opcion == "2":
            numero = int(input("Por favor, ingrese un numero entero: "))
            cantidad_digitos = contar_digitos(numero)
            print("El numero ", numero, "tiene ", cantidad_digitos, " digitos.")
        elif opcion == "3":
            numero=float(input("Ingrese un numero: "))
            print("Raiz cuadrada entera de ", numero, "es: ", raiz_cuadrada_entera(numero))
        elif opcion == "4":
            num=input("Por favor, ingrese el numero entero a convertir en numero romano: ")
            try:
                num = int(num)
                if(num > 0 and num <= 3999):
                    print(f"El numero romano es: {normal_a_romano(num)}")
                else:
                    print(f"Por favor, ingresa un numero entre 1 y 3999.")
            except ValueError:
                print("Por favor, ingrese unicamente numeros enteros")
        elif opcion == "5":
            numero = int(input("Ingrese el valor hasta el cual desea sumar: "))
            print(suma_numeros_enteros(numero))
        elif opcion=="6":
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion valida.")
main()   