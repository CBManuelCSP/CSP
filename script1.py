longitud_str = input("Introduce la longitud: ")
anchura_str = input("Introduce la anchura: ")

longitud = float(longitud_str)
anchura = float(anchura_str)

area = longitud * anchura
print("El área del rectángulo es: ", area)

# Agora con un círculo
radio = float(input("Introduce el radio del círculo (Modificación local)"))
print("El área del círculo es ", radio*radio*3.14)