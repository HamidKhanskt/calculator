def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def display_menu():
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid choice. Please enter a number.")


def calculator():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def main():
    print("Welcome to Simple Calculator!")
    calculator()

if __name__ == "__main__":
    main()
