roomtemperatura = int(input("Enter the room temperature in Celsius: "))
if roomtemperatura >= 30:
    print("Alert: temperature above the recommended level.")
elif roomtemperatura <= 15:
    print("Alert: temperature below the recommended level.")
else: print("The room temperature is in the recommended level.")