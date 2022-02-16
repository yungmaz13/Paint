import turtle as g

colours=["black","grey","white","red","yellow","pink","green","orange","violet","purple","blue","aqua","lime"]
colour=colours[0]

s=g.Screen()
s.setup(1.0,1.0)
s.title("Paint")
s.bgcolor("white")

Map=[[str()for _ in range(s.window_width())]for _ in range(s.window_height())]

c=s.getcanvas()

p=g.Turtle("circle")
p.color(colour)
p.speed(0)
p.penup()

corrector=p.clone()
corrector.ht()

def addWidth():
    p.shapesize(p.shapesize()[0]+1)
def addHeight():
    p.shapesize(stretch_len=p.shapesize()[1]+1)
def addBoth():
    p.shapesize(p.shapesize()[0]+1,p.shapesize()[1]+1)

def minusWidth():
    if p.shapesize()[0]>1:p.shapesize(p.shapesize()[0]-1)
def minusHeight():
    if p.shapesize()[1]>1:p.shapesize(stretch_len=p.shapesize()[1]-1)
def minusBoth():
    if p.shapesize()[0]>1:p.shapesize(p.shapesize()[0]-1)
    if p.shapesize()[1]>1:p.shapesize(p.shapesize()[1]-1)

draw=False
def penup(x,y):
    global draw
    draw=False
def pendown(x,y):
    global draw
    draw=True

def pixeltocartesian(x:float,y:float):
    w,h=c.winfo_width(),c.winfo_height()
    xp,xc=list(range(w+1)),list(range(-w//2,w//2+1))
    yp,yc=list(range(h+1)),list(range(-h//2,h//2+1))
    return xc[xp.index(x)]-2,-yc[yp.index(y)]+20

def blink(x,y):
    if p.isvisible():p.ht()
    else:p.st()

def dragging(x,y):
    p.ondrag(None)
    p.stamp()
    Map[p.ycor()][p.xcor()]=p.fillcolor()
    p.ondrag(dragging)

def switchcolour():
    global colour
    try:
        colour=colours[colours.index(colour)+1]
    except IndexError:
        colour=colours[0]
    p.color(colour)

s.onkeypress(switchcolour,"z")
p.ondrag(dragging)
s.onscreenclick(blink,2)
for i,j in enumerate((minusWidth,addWidth,minusHeight,addHeight,minusBoth,addBoth),1):s.onkeypress(j,str(i))
s.onkeypress(p.clear,"c")
for i in "q","e":s.onkeypress(s.bye,i)
s.listen()
while True:
    try:
        p.goto(pixeltocartesian(*c.winfo_pointerxy()))
        s.update()
    except Exception as e:print(e)
