num = int(input("Enter the number : "))

if num == 1:
    print("Not a prime number")

if num > 1:
    for i in range (2, num):
        if num % i == 0:
            print("it is not a prime number")
        else: 
            print("It is a prime number")