idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Proibido votar.")
elif 16 <= idade < 18 or idade >= 65:
    print("Voto optativo.")
else:
    print("Voto obrigatório.")