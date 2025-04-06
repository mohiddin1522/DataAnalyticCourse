num = int(input("Enter a number: "))

num1 = 0
num2 = 1
while(num1 < num):
    print(num1)
    res = num1 + num2
    num1 = num2
    num2 = res