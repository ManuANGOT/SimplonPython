import turtle

turtle.speed(1)
window = turtle.Screen()

# Création d'un objet Turtle
t = turtle.Turtle()

# Carré
for _ in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.forward(150) 
t.pendown()

# Pentagone
for _ in range(5):
    t.forward(100)
    t.right(72)

# Déplacement pour dessiner le bateau
t.penup()
t.forward(200)  
t.pendown()

# Bateau
t.right(135)
t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(142)
t.left(135)
t.forward(100)
t.left(90)
t.forward(100)

window.exitonclick()