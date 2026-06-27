print("===== Calculator =====")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("\nSelect an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice (1/2/3/4): ")
if choice == "1":
    result = n1+n2
    print("Result =", result)
elif choice == "2":
    result = n1-n2
    print("Result =", result)
elif choice == "3":
    result = n1*n2
    print("Result =", result)
elif choice == "4":
    if num2 != 0:
        result = n1/n2
        print("Result =", result)
    else:
        print("Error! Division by zero is not allowed")
else:
    print("Invalid choice. Please select a valid operation")
print("Thank you for using the calculator!")
