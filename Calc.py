def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            # Get input from user
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on operator
            if op == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif op == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif op == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid operator! Please use +, -, *, or /")
            
            # Ask if user wants to continue
            again = input("Calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    calculator()