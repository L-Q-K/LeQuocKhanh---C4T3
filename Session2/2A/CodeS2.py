import os

h = float(input('Nhap chieu cao (cm ): '))
w = float(input('Bao nhiau can (kg) : '))
bmi = w/(h/100)**2
if bmi < 16:
    print('Quá gầy')
elif bmi < 18.5:
    print('Hơi gầy')
elif bmi < 25 :
    print('Body chuẩn')
elif bmi < 30:
    print('Béo')
else:
    print('Mập đuỵt')

input("Enter để qua bài mới")
os.system('cls')

n = int(input("Nhập n: "))

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i
print ("Giai thừa của", n, "là:", factorial)

input("Enter để qua bài mới")      
os.system('cls')

for i in range(20):
    print(i, end=' ')
    
print()

n = int(input("Nhập n: "))

for i in range(n):
    print(i, end=' ')

print()

for i in range(20):
    if i % 2 == 0:
        print(1, end=' ')
    else:
        print(0, end=' ')

print()

n = int(input("Nhập n: "))

for i in range(n):
    if i % 2 == 0:
        print(1, end=' ')
    else:
        print(0, end=' ')

input("Enter để qua bài mới")
os.system('cls')

print("WARNING: OPTIONAL!!!")
for i in range(1,10):
    for j in range(i, i*9+1, i):
        print(j, end=" ")
    print()

n = int(input("Nhập n: "))

for i in range(1,n+1):
    for j in range(i, i*n+1, i):
        print(j, end=" ")
    print()

print()

for i in range(10):
    for j in range(10):
        if i % 2 == 0:
            if j % 2 == 0:
                print(1, end=' ')
            else:
                print(0, end=' ')
        else:
            if j % 2 == 0:
                print(0, end=' ')
            else:
                print(1, end=' ')
    print()

n = int(input("Nhập n: "))

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                print(1, end=' ')
            else:
                print(0, end=' ')
        else:
            if j % 2 == 0:
                print(0, end=' ')
            else:
                print(1, end=' ')
    print()

print("2.a End")
input("Enter để thoát")
        
