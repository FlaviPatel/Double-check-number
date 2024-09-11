# We have to check whether the number entered by the user is greater than 50. Also we have to check if the number is odd or even.

num = int(input("Enter a number: "))

if num > 50:
    print(num, "It is greater than 50")
    if num % 2 == 0:
        print("also it is even")
    else:
        print("also it is odd")

else:
    print(num, "is not greater than 50")