import os
import random

items = ['T-shirts','Sweater']
print("Q to quit")
while True:
    
    action = input('Welcome t’o our shop, what do you want (C, R, U, D)?').lower()
    if action == 'c':
        items.append(input('New item: '))
        print(items)
    elif action =='r':
        print(items)
    elif action =='u':
        p = int(input('Position?')) - 1
        i = input('Item?:')
        items[p] = i
        print(items)
    elif action =='d':
        del items[int(input('Position? '))-1]
        print(items)
    elif action =='q':
        break
    else:
        print('we don\'t  offer that, GTFO')

os.system('cls')

flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Khanh and these are my sheep size: ')
print(flock)

print('Now my biggest sheep has size', max(flock),' let\'s shear it')

flock[flock.index(max(flock))] = 8                                                  
print('After shearing, hear is my flock ')
print(flock)

flock = [x+50 for x in flock]                           
print('1 month has passed , here is my flock: ')
print(flock)

input("Enter để qua bài mới")        
os.system('cls')

flock = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Khanh and these are my sheep size: ')    
print(flock)

for _ in range(4):
    print()
    
    print('Month', _ + 1)
    flock = [x+50 for x in flock]                                                            
    print('1 month has passed , here is my flock: ')
    print(flock)
    
    print('Now my biggest sheep has size', max(flock),' let\'s shear it')
    flock[flock.index(max(flock))] = 8
    
    print('After shearing, hear is my flock ')
    print(flock)

print()
    
print('I\'m bored with this')
t = 0
for i in flock:
    t += i
print('My flock has size in total: ',t)
print('So i would get : ',t, ' *2$ = ', t*2 ,'$')
print("2 bài cuối em gộp nên kết quả hơi khác mẫu ạ")

input("Enter để qua bài mới")        
os.system('cls')

print("Welcome to word jumble game!!!")
print("Demo với 10 từ :(")
print()

while True:
    words = ["compromise", "entrepreneur", "rather", "persuade", "include", "peopleintegrity", "talented", "perspective", "discrimination"]
    word = words[random.randint(0, len(words) - 1)]

    alphabet = list(word)
    random.shuffle(alphabet)
    print(*alphabet, sep=" ")

    while True:
        answer = input("Your answer: ").lower()
        answer = answer.replace(" ", "")
        if answer == word:
            print("Hura you're so lucky")
            print()
            break
        else:
            print("Try again")
            print()

    action = input("Again? Y/N").lower()
    action = action.replace(" ", "")
    if action == 'n':
        break


