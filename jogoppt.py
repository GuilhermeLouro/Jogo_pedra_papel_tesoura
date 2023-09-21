#jogo pedra papel ou tesoura
#
# Autor: Guilherme Louro    V:0.0

# 01 - Instânciar as variáveis

import random

user = input("Escolha uma opção:")
pc = random.choice(("pedra", "papel", "tesoura"))

# 02 - Lógica
if user == "papel" and pc == "papel": 
    resultado = "Empate"

if user == "tesoura" and pc == "papel":
    resultado = "Jogador Vence"

if user == "pedra" and pc == "papel":
    resultado = "Jogador perde"

if user == "papel" and pc == "tesoura":
    resultado = "Jogador Perde"
if user == "tesoura" and pc == "tesoura":
    resultado = "Empate"
if user == "pedra" and pc == "tesoura":
    resultado = "Jogador vence"
if user == "papel" and pc == "pedra":
    resultado = "Jogador vence"
if user == "tesoura" and pc == "pedra":
    resultado = "Jogador perde"
if user == "pedra" and pc == "pedra":
    resultado = "Empate"




# 03 - Resultado
print(resultado)
print("user", user, "pc", pc)
