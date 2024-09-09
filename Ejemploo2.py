
def suma(sumando1, sumando2):
    suma = sumando1 + sumando2
    return suma

def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto


if __name__ == "__main__":

    sumando1 = float(input("Ingrese el Sumando 1: "))
    sumando2 = float(input("Ingrese el Sumando 2: "))

    sumaT = suma(sumando1, sumando2)

    print(f"El multiplicador es: {sumaT}")

    multiplicando = float(input("Ingrese el Multiplicando: "))
    resultado = multiplicacion(sumaT, multiplicando)
    print("El resultado es:", resultado)

