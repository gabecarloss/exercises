#João é atendente em uma farmácia e precisa verificar se um cliente forneceu um número de receita válido em uma descrição. O número da receita é sempre o único número presente no texto fornecido pelo cliente. Ele quer um programa que extraia esse número diretamente e confirme se o texto está correto, sem a necessidade de trabalhar com listas ou loops.
#Com base nesse cenário, crie um programa que receba um texto com uma descrição e exiba uma mensagem com o número encontrado.
import re
description = input("Write the recipe description: ")
number = re.findall(r'\d+', description)[0]
print(f"The recipe number is: {number}")