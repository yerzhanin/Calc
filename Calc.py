while True:
    try:
        number_a = float(input("Enter first number: "))
        number_b = float(input("Enter second number: "))
    except ValueError:
        print("String is not allowed")
    operation = input("Enter operation: ")
    if operation == '+':
        print(number_a + number_b)
    elif operation == '-':
        print(number_a - number_b)
    elif operation == '*':
        print(number_a * number_b)
    elif operation == '/':
        print(number_a / number_b)

    break
