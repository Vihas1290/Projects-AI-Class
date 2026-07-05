command = input("Command: ")

while command != "quit":
    if command.startswith("echo"):
        print(command[4:])
        command = input("Command: ")
    elif command.startswith("add"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        print(int(x) + int(y))
        command = input("Command: ")
    elif command.startswith("subtract"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        print(int(x) - int(y))
        command = input("Command: ")
    elif command.startswith("multiply"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        print(int(x) * int(y))
        command = input("Command: ")
    elif command.startswith("divide"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        if int(y) == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(int(x) / int(y))
        command = input("Command: ")
    elif command.startswith("help"):
        print("Available commands: echo, add, subtract, multiply, divide, help, quit")
        command = input("Command: ")
    elif command.startswith("compare(><)"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        if int(x) > int(y):
            print(f"{x} is greater than {y}")
        elif int(x) < int(y):
            print(f"{x} is less than {y}")
        else:
            print(f"{x} is equal to {y}")
        command = input("Command: ")
    elif command.startswith("compare(even/odd)"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        if int(x) % 2 == 0 and int(y) % 2 == 0:
            print(f"Both {x} and {y} are even")
        elif int(x) % 2 != 0 and int(y) % 2 != 0:
            print(f"Both {x} and {y} are odd")
        else:
            print(f"{x} and {y} are of different parity")
        command = input("Command: ")
    elif command.startswith("compare(odd/even)"):
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        if int(x) % 2 == 0 and int(y) % 2 == 0:
            print(f"Both {x} and {y} are even")
        elif int(x) % 2 != 0 and int(y) % 2 != 0:
            print(f"Both {x} and {y} are odd")
        else:
            print(f"{x} and {y} are of different parity")
        command = input("Command: ")
    else: 
        print("Unknown command. Type 'help' for a list of available commands.")
        command = input("Command: ")