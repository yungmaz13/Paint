import turtle as t

colours=["black","grey","white","red","yellow","pink","green","orange","violet","purple","blue","aqua","lime"]
colour=colours[0]

Screen=t.Screen()
Screen.setup(1.0,1.0)
Screen.title("Paint")
Screen.bgcolor("white")

Canvas=Screen.getcanvas()

Brush=t.Turtle("circle")
Brush.color(colour)
Brush.speed(0)
Brush.penup()

def addWidth():
    Brush.shapesize(Brush.shapesize()[0]+1)
def addHeight():
    Brush.shapesize(stretch_len=Brush.shapesize()[1]+1)
def addBoth():
    Brush.shapesize(Brush.shapesize()[0]+1,Brush.shapesize()[1]+1)

def minusWidth():
    if Brush.shapesize()[0]>1:
        Brush.shapesize(Brush.shapesize()[0]-1)
def minusHeight():
    if Brush.shapesize()[1]>1:
        Brush.shapesize(stretch_len=Brush.shapesize()[1]-1)
def minusBoth():
    if Brush.shapesize()[0]>1:
        Brush.shapesize(Brush.shapesize()[0]-1)
    if Brush.shapesize()[1]>1:
        Brush.shapesize(Brush.shapesize()[1]-1)

draw=False
def penup(x,y):
    global draw
    draw=False
def pendown(x,y):
    global draw
    draw=True

def pixeltocartesian(x:float,y:float):
    w,h=Canvas.winfo_width(),Canvas.winfo_height()
    xp,xc=list(range(w+1)),list(range(-w//2,w//2+1))
    yp,yc=list(range(h+1)),list(range(-h//2,h//2+1))
    return xc[xp.index(x)]-2,-yc[yp.index(y)]+20

def blink(x,y):
    if Brush.isvisible():
        Brush.ht()
    else:
        Brush.st()

def dragging(x,y):
    Brush.ondrag(None)
    Brush.stamp()
    Brush.ondrag(dragging)

def switchcolour():
    global colour
    try:
        colour=colours[colours.index(colour)+1]
    except IndexError:
        colour=colours[0]
    Brush.color(colour)

Screen.onkeypress(switchcolour,"z")
Brush.ondrag(dragging)
Screen.onscreenclick(blink,2)
for i,j in enumerate((minusWidth,addWidth,minusHeight,addHeight,minusBoth,addBoth),1):
    Screen.onkeypress(j,str(i))
Screen.onkeypress(Brush.clear,"c")
for i in "q","e":
    Screen.onkeypress(Screen.bye,i)

Screen.listen()
while True:
    try:
        Brush.goto(pixeltocartesian(*Canvas.winfo_pointerxy()))
        Screen.update()
    except Exception as e:
        print(e)

print()
