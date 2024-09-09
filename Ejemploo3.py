# Función para calcular el área de un rectángulo
def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    areaT = 0.5 * base * altura
    return areaT

if __name__ == "__main__":


# Función principal
def main():
    multiplicando = float(input("Multiplicando: "))
    multiplicador = float(input("Multiplicador: "))
    rect_area = multiplicacion(multiplicando, multiplicador)
    print("Área del rectángulo:", rect_area)

    base = float(input("Base: "))
    altura= float(input("Altura: "))
    tri_area = area_triangulo(base, altura)
    print("Área del triángulo:", tri_area)

main()
