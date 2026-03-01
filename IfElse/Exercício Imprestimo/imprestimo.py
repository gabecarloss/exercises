rent = float(input("Enter the monthly rental amount: "))
bills = float(input("Enter the value of the bill: "))
if bills > 0.3 * rent:
    print("Alert: bill exceeds 30% of the rent.")
else: print("The bill is within the acceptable range.")