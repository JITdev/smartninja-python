first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operand = input("Enter the operand (+ - * /): ")

if operand == "+":
    print(first_num + second_num)
elif operand == "-":
    print(first_num - second_num)
else:
    print()