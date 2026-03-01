#Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. O padrão esperado é que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.
#Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.
import re
name = input("Writhe your name:"  )
pattern = r"^[A-Z][a-z]*$"
if re.match(pattern, name):
    print("Valid name!")
else:
    print("Invalid name, your name should start with a capital letter and contain only letters.")