operator="+ - * /"
number=float(input("Enter the first number"))
operators=operator=input('enter operator (+,-,*,/): ')
number1=float(input("enter the second number"))
if operator=='+':
    print(number+number1)
elif operator=='*':
    print(number*number1)
elif operator=='/':
    print(number/number1)
