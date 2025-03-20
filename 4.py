operadores= ["+","-","*","/"]
num1=int(input("insira o primeiro numero"))
num2=int(input("insira o segudo numero"))
operador= str(input("insira o operador para o calculo"))
if operador in operadores:
  if operador == operadores[0]:
    print(num1+num2)
  elif operador == operadores [1]:
    print(num1-num2)
  elif operador == operadores [2]:
    print(num1*num2)
  elif operador == operadores [3]:
    print(num1/num2)
else:
  print("operador invalido")