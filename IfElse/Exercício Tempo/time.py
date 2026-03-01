task1 = int(input("Enter how many days take to complete the task 1: "))
task2 = int(input("Enter how many days take to complete the task 2: "))
task3 = int(input("Enter how many days take to complete the task 3: "))

if task1 <= 0 or task2 <= 0 or task3 <= 0:
    print("Error: The numbers of days must be positive.")
elif task1 >= 1 and task2 >= 1 and task3 >= 1:
    total_days = task1 + task2 + task3
    print(f"The total time to complete all tasks is: {total_days} days.")