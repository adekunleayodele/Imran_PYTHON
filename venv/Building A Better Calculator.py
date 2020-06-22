
num1 = float(input("Enter first number"))
oper = float(input("Enter operation"))
num2 = float(input("Enter second number"))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid operator")