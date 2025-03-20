lado1= int(input("insira o valor de um lado de um triangulo: "))
lado2= int(input("insira o valor de um lado de um triangulo: "))
lado3= int(input("insira o valor de um lado de um triangulo: "))

match (lado1 == lado2, lado1 == lado3, lado2 == lado3):
  case 1, 1, 1:
    print("o triangulo é equilatero")
  case 0, 0, 0:
    print("o triangulo é escaleno")
  case _:
    print("o triangulo é isosceles")