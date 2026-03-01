estoque = 5
while estoque >= 0:
    print ("Venda realizada! Estoque restante:", estoque)
    estoque -= 1
    if estoque < 0:
        print("Estoque esgotado!")