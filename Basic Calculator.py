print("Basic Calculator")
print("-----------------")

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = (num1+num2)
elif operator == "-":
    result = (num1-num2)
elif operator == "*":
    result =(num1*num2)
elif operator == "/":
    result = (num1//num2)
elif operator == "%":
    result = (num1%num2)
else:
    print("Invalid operator. Please enter a valid operator.")

print(f"Result: {num1} {operator} {num2} = {result}")
