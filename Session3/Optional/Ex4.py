from math import *
print("Input nothing to quit")

while True:
    bln = True
    n = input("Enter a number: ")
    try:
        if "." in n:
            print("It is not an invalid number")
        else:
            n = int(n)
            if n < 0:
                print("It is not an invalid number")
            elif n <= 2:
                print(n, "is a prime number")
            else:
                for i in range(2, n):
                    if n % i == 0:
                        bln = True
                        print(n, "isn't a prime number")
                        break
                    else:
                        bln = False
                if bln == False:
                    print(n, "is a prime number")
    except:
        break

            
    
