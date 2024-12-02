num1=input("enter your first number:")
num2=input("enter your second number:")

print("Choose Operation")
print("1. Add\n2.Subtract\n3.Multiply\n4.Divide")

op = input("Enter operation:")

try:
    num1 = int(num1)
    num2 = int(num2)
    op = int(op)
except:
    print("Invalid input.")

if(op == 1):
    sum = num1 + num2
    print(num1, "+", num2, "=", sum)
elif(op == 2):
    minus = num1 - num2
    print(num1, "-", num2, "=", minus)
elif(op == 3):
    mult= num1 * num2
    print(num1, "*", num2, "=", mult)

elif(op == 4):
    div= num1/num2
    print(num1, "/", num2, "=",div)
else:
    print("error")