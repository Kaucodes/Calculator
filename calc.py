import math

def get_two_numbers():
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        return num1, num2
    except ValueError:
        print("Invalid number entered.")
        return None, None
    
print("""
Select an operation to perform: 
\t1. ADD
\t2. SUBTRACT
\t3. MULTIPLY
\t4. DIVIDE
\t5. SQUARE ROOT
\t6. RAISE TO POWER
""")
operation = input(">> ")
match operation:
    case "1": # PERFORM ADDITION
        num1, num2 = get_two_numbers()
        if num1 is not None:
            result = num1 + num2
            print(F"The sum is {result}")

    case "2": # PERFORM SUBTRACTION
        num1, num2 = get_two_numbers()
        if num1 is not None:
            result = num1 - num2
            print(F"The difference is {result}")

    case "3": # PERFORM MULTIPLICATION
        num1, num2 = get_two_numbers()
        if num1 is not None:
            result = num1 * num2
            print(F"The product is {result}")

    case "4": # PERFORM DIVISION
        num1, num2 = get_two_numbers()
        if num1 is not None:
            try:
                result = num1 / num2
                print(F"The result is {result}")
            except ZeroDivisionError:
                print("Cannot divide by zero.")

    case "5": # PERFORM SQUARE ROOT
        try:
            num = float(input("Enter number: "))
            result = math.sqrt(num) # import math usage
            print(F"The square root is {result}")
        except ValueError:
            print("Invalid number entered.")

    case "6":
        try:
            num = float(input("Enter number: "))
            power = float(input("Raise power to: "))
            result = pow(num, power)
            print(F"The result is {result}")
        except ValueError:
            print("Invalid number entered.")

    case _:
        print("Invalid Entry!")