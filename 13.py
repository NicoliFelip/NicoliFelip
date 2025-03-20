salario = float(input("Digite o valor do salário: "))

if salario <= 280:
    aumento = salario * 0.20
elif salario <= 700:
    aumento = salario * 0.15
elif salario <= 1500:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento
print(f"Novo salário após reajuste: R$ {novo_salario:.2f}")