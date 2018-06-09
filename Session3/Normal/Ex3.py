numbers = [1, 6, 8, 1, 2, 1, 5, 6]
print("Input nothing to quit")

print(numbers)
while True:
    n = input("Enter a number: ")
    count = 0
    
    try:
        n = int(n)
        for i in numbers:
            if i == n:
                count += 1
    except:
        break

    print(n, "appears in my list", count, "times")

    
    

