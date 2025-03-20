def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Você quer converter Celsius para Fahrenheit (C) ou Fahrenheit para Celsius (F)? ").strip().upper()

if opcao == "C":
    temp = float(input("Digite a temperatura em Celsius: "))
    print(f"{temp}°C equivale a {celsius_para_fahrenheit(temp):.2f}°F")
elif opcao == "F":
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{temp}°F equivale a {fahrenheit_para_celsius(temp):.2f}°C")
else:
    print("Opção inválida. Escolha 'C' ou 'F'.")