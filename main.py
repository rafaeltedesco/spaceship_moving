import turtle

wn = turtle.Screen()
wn.setup(800, 600)


sprites = [a + '.gif' for a in ['t', 'r', 'd', 'l']]

for shape in sprites:
  wn.register_shape(shape)


player = turtle.Turtle()
player.sprites = sprites
player.penup()
player.current_sprite = player.shape(player.sprites[0])
player.seth(90)
player.velocity = 20


def up():
  player.seth(90)
  player.shape(player.sprites[0])
  

def right():
  player.seth(0)
  player.shape(player.sprites[1])
  

def down():
  player.seth(270)
  player.shape(player.sprites[2])
  

def left():
  player.seth(180)
  player.shape(player.sprites[3])

wn.onkey(up, 'w')
wn.onkey(right, 'd')
wn.onkey(down, 's')
wn.onkey(left, 'a')

def move():
  player.fd(player.velocity)

wn.listen()

while True:
  
  wn.ontimer(move(), 100)
  if player.xcor() > 320:
    left()
  elif player.xcor() < -300:
    right()
  elif player.ycor() > 220:
    down()
  elif player.ycor() < -200:
    up()
  