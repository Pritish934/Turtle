from turtle import *
pencolor('white')
speed(0)
bgcolor('black')
fillcolor('#b32d00')
begin_fill()
for i in range(60):
    forward(3)
    left(1)
penup()
goto(0,0)
left(120)
pendown()
for i in range(60):
    forward(3)
    right(1)

right(120)
for i in range(40):
    forward(4)
    left(0.8)
right(63)
for i in range(39):
    forward(4)
    left(0.8)
end_fill()
penup()
for i in range(39):
    left(-0.8)
    forward(-4)

left(176)
pendown()
fillcolor('#ffff33')
begin_fill()
for i in range(60):
    forward(0.5)
    right(0.6)
for i in range(30):
    forward(0.4)
    right(0.5)

for i in range(70):
    forward(0.5)
    right(0.5)
for i in range(40):
    forward(0.5)
    left(0.3)
right(160)
for i in range(54):
    forward(0.5)
    left(0.5)
for i in range(30):
    forward(0.5)
    right(0.5)
for i in range(40):
    forward(0.8)
    right(0.5)
for i in range(17):
    forward(1)
    right(2.5)
end_fill()
penup()
goto(20,-35)
write("Happy diwali", font=("Verdana",20, "normal"))
hideturtle()
done()