numero= int(input("insira um numero de 1 ate o 7  "))

match numero:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")
    case 4:
        print("quarta")
    case 5:
        print("quinta")
    case 6:
        print("sexta")
    case 7:
        print("sábado")
    case _:
        print("numero invalido")