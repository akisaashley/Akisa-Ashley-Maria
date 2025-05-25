while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
    else:
        print(f"The result of dividing {num1} by {num2} is: {result}")
        break
