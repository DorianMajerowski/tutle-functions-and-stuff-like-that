import turtle as t

t.speed(0)

def drawRect(x, y, lenX, lenY):
	t.penup()
	t.goto(x, y)
	t.pendown()
	for i in range(2):
		t.forward(lenX)
		t.right(90)
		t.forward(lenY)
		t.right(90)

def drawSqu(x, y, leng):
	drawRect(x, y, leng, leng)

def drawIsoTri(x, y, leng):
	t.penup()
	t.goto(x, y)
	t.pendown()
	for i in range(3):
		t.forward(leng)
		t.left(120)

drawSqu(-125, 125, 250)

drawRect(-100, 0, 75, 125)

drawSqu(10, 10, 100)

drawIsoTri(-125, 125, 250)