#Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada. 
#Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

secret_word = input("Write the key word: ")
print("First ones:", secret_word[0:3])
print("Last ones:", secret_word[-3:])