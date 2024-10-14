def calculator():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation (+, -, *, /): ")


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"


    print( "The result is: ",result)
    choose=input("If you still want to calculate some more problems (1/0)")
    if choose =='1':
        calculator()
    else:
        exit()


print(calculator())
