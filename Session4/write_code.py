font = int(input("Size of word you want ?:(3<n<10 = perfect) "))

def print_star():
    print("* ", end="")

def first_last():
    for i in range(4):
        for j in range(font):
            if i == 2 and j == font - 1:
                print("  ", end="")
            else:
                print_star()
                
        print(" " * font, end="")
    
    print()

def middle_lines(i, j):
    if (i == 0 and j == 0)\
        or (i == 1 and (j == 0 or j == font - 1))\
        or (i == 2 and (j == 0 or j == font - 1))\
        or (i == 3 and (j == 0)):

        print_star()

    else:
        print("  ", end="")

def middle_line(i, j):
    if (i == 0 and j == 0)\
        or (i == 1 and (j == 0 or j == font - 1))\
        or (i == 2 and (j == 0 or j == font - 1)):

        print_star()
    elif i == 3:
        print_star()
    else:
        print("  ", end="")

for _ in range(font):
    if _ == 0 or _ == font - 1:
        first_last()
    else:
        for i in range(4):
            for j in range(font):
                if font % 2 == 0:
                    if _ == (font // 2) - 1:
                        middle_line(i, j)
                    else:
                        middle_lines(i, j)
                else:
                    if _ == font // 2:
                        middle_line(i,j)
                    else:
                        middle_lines(i, j)
                    
            print(" " * font, end="")
            
        print()
            
input("Enter to leave")       
