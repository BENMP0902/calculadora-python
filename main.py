from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada


def menu():
   while True:  
    print("\nCalculadora en Python")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado de la suma es: ", sumar(a,b))
    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado de la resta es: ", restar(a,b))
    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado de la multiplicación es: ", multiplicar(a,b))
    elif opcion == 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado de la división es: ", dividir(a,b))
    elif opcion == 5:
        numeros = []
        cantidad = int(input("¿Cuántos números desea sumar? "))
        for i in range(cantidad):
            numeros.append(float(input("Ingrese el número: ")))
        print("El resultado de la suma avanzada es: ", suma_avanzada(*numeros))
    elif opcion == 6:
        print("saliendo...")
        break
    else:
        print("Opción no válida")

if __name__ == "__main__":
    menu()
