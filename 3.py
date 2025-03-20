num1=int(input("insira o primeiro numero"))
num2=int(input("insira o segudo numero"))
operador= str(input("insira o operador para o calculo"))

if operador == "+":
    print(num1+num2)
elif operador == "-":
    print(num1-num2)
elif operador == "*":
    print(num1*num2)
elif operador == "/":
    print(num1/num2)
else:
  print("operador invalido")