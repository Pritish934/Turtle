from turtle import *
speed(2000)
penup()
goto(10,100)
left(180)
pendown()
fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(150)
    for i in range(60):
        forward(1)
        left(1.5)
end_fill()      
penup()
forward(75)
left(90)
forward(40)
right(93)
# clone head
pendown()
pensize(3)
fillcolor('white')
begin_fill()
for i in range(60):
    forward(0.5)
    left(0.5)
for i in range(40):
    forward(0.5)
    left(1)
for i in range(15):
    forward(1)
    left(1.5)
forward(18)
right(93)
# end of head
# right hand start
for i in range(15):
    right(0.9)
    forward(0.5)
for i in range(10):
    forward(0.5)
    left(0.5)
for i in range(50):
    left(3)
    forward(0.2)
left(15)
for i in range(27):
    forward(0.5)
    left(0.1)  
for i in range(30):
    right(3)
    forward(0.2)

for i in range(27):
    forward(1.5)
    right(0.5)
for i in range(45):
    forward(0.5)
    right(1.2)
for i in range(54):
    left(3)
    forward(0.1)
for i in range(47):
    forward(0.5)
    left(0.3)
right(80)
forward(8)
left(90)
for i in range(30):
    forward(0.5)
    right(0.2)
for i in range(30):
    forward(0.2)
    right(1.4)
for i in range(10):
    forward(0.2)
    left(0.5)
for i in range(9):
    forward(0.3)
    right(0.5)
for i in range(10):
    forward(0.5)
    left(0.2)
for i in range(81):
    forward(0.9)
    left(1)
for i in range(5):
    left(0.2)
    forward(0.5)
for i in range(10):
    right(0.5)
    forward(0.3)
for i in range(10):
    left(0.5)
    forward(0.2)
for i in range(30):
    forward(0.2)
    right(1.4)
for i in range(30):
    right(0.2)
    forward(0.5)
left(90)
forward(8)
right(80)
for i in range(47):
    left(0.3)
    forward(0.5)
for i in range(54):
    forward(0.1)
    left(3)
for i in range(45):
    right(1.2)
    forward(0.5)
for i in range(27):
    right(0.5)
    forward(1.5)
for i in range(30):
    forward(0.2)
    right(3)
for i in range(27):
    left(0.1)
    forward(0.5)
left(15)
for i in range(50):
    forward(0.2)
    left(3)
for i in range(10):
    left(0.5)
    forward(0.5)
for i in range(15):
    forward(0.5)
    right(0.9)
right(93)
forward(18)
for i in range(15):
    left(1.5)
    forward(1)
for i in range(60):
    left(0.5)
    forward(0.5)
end_fill()
hideturtle()
done()