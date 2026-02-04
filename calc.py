print("Mini Calculator")

num1 = int(input("Enter the first number : "))
operation = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter the second number : "))

if operation == "+":
    result = num1 + num2
    Output = result
    print("Output :", Output)

elif operation == "-":
    result = num1 - num2
    Output = result
    print("Output :", Output)

elif operation == "*":
    result = num1 * num2
    Output = result
    print("Output :", Output)

elif operation == "/":
    result = num1 / num2
    Output = result
    print("Output :", Output)

    

