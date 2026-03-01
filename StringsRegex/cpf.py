import re
cpf = input("Write CPF number in the format XXX.XXX.XXX-XX: ")
cpf_pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
if re.match(cpf_pattern, cpf):
    print("Valid CPF number!")
else:    
    print("Invalid CPF number, please enter numbers in the format XXX.XXX.XXX-XX.")