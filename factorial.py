number = input("Enter a number.")
num = int(number)
factorial = 1
if num == 0:
    print(1)
elif num == 1:
    print(1)
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(factorial)