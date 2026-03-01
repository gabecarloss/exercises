wheight = int(input("Enter the weight in kilograms: "))

height = float(input("Enter the height in meters: "))

imc = wheight / (height ** 2)
print(f"The IMC is: {imc:.2f}")
if imc <= 18.5:
    print("Underweight")
elif imc >= 25:
    print("Overweight")
else:
    print("Normal weight")