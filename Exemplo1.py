nome = (input("Qual é o seu nome? "))
idade = int(input("Qual é sua idade? "))

if idade >= 18:
    ValidaIdade = "maior"

else:
    ValidaIdade = "menor"

print("Bem vindo %s, você é %s de idade." %(nome, ValidaIdade))