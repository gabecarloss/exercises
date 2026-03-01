segundos = 10
for i in range(10):
    segundo = segundos - i
    if segundo % 2 == 0:
        print("Faltam apenas", segundo, "segundos, não perca essa oportunidade!")
    elif segundo % 2 != 0:
        print("A contagem continua:", segundo, "segundos restantes.")