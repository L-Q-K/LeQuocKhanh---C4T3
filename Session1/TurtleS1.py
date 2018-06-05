from turtle import *
import time

speed(50)
shape ('turtle')
pencolor ('Red')
pensize(15)
#square
for i in range(4):
    forward(100)
    left(90)
time.sleep(3)

clearscreen()

shape ('turtle')
pencolor ('teal')
pensize(15)
speed(50)

#ultra-multi-square
for i in range(30):
    for j in range(4):
        forward(i*5)
        left(90)
    forward(i*2)
    right(15)

time.sleep(3)

clearscreen()

shape ('turtle')
pencolor ('purple')
pensize(15)
speed(50)

#multi-square
for i in range(20):
    for j in range(4):
        forward(100)
        left(90)
    right(30)
time.sleep(3)

clearscreen() 
        
shape ('turtle')
pencolor ('yellow')
pensize(15)
speed(50)

#triangle
left(60)
for i in range(3):
    right(120)
    forward(200)
time.sleep(3)

clearscreen()

shape ('turtle')
pencolor ('black')
pensize(15)
speed(50)

#circle
circle(80)
right(20)
time.sleep(3)

clearscreen()

#multi-cirlce

write('Even better =))',font=('.VnBahamasB',64,'normal'))
time.sleep(1)
clearscreen()

shape ('turtle')
pencolor ('orange')
pensize(15)
speed(-1)
for i in range(1, 500, 50):
    right(90)
    forward(i)
    right(270)
    pendown()
    circle(i)  
    penup()    
    home()

time.sleep(2)
clearscreen()


shape ('turtle')
pencolor ('orange')
pensize(15)
speed(50)

for i in range(100):
    circle(80)
    right(20)

clearscreen()

write('10 <3',font=('.VnBahamasB',72,'normal'))


