import turtle as t

Colours=["black","grey","white","red","yellow","pink","green","orange","violet","purple","blue","aqua","lime"]
Colour=Colours[0]

Screen=t.Screen()
Screen.setup(1.0,1.0)
Screen.title("Paint")
Screen.bgcolor("white")
Screen.tracer(0,0)

Canvas=Screen.getcanvas()

Brush=t.Turtle("circle")
Brush.color(Colour)
Brush.speed(0)
Brush.penup()
Brush.pensize(16)

w,h=Canvas.winfo_width(),Canvas.winfo_height()
xp,xc=range(w+1),range(-w//2,w//2+1)
yp,yc=range(h+1),range(-h//2,h//2+1)
def PixelToCartesian(x:float,y:float):
    const=5
    try:
        return xc[xp.index(x)]-const,-yc[yp.index(y)]+const*10
    except ValueError:
        return xc[xp.index(x)]-const,-yc[-1]+const*5

def IncreaseSize():
    Brush.shapesize(Brush.shapesize()[0]+1,Brush.shapesize()[1]+1)
    Brush.pensize(Brush.shapesize()[0]*16)

def DecreaseSize():
    if Brush.shapesize()[0]>1:
        Brush.shapesize(Brush.shapesize()[0]-1)
    if Brush.shapesize()[1]>1:
        Brush.shapesize(Brush.shapesize()[1]-1)
    Brush.pensize(Brush.shapesize()[0]*16)

def Blink(x,y):
    if Brush.isvisible():
        Brush.ht()
    else:
        Brush.st()

def SwitchColour():
    global Colour
    try:
        Colour=Colours[Colours.index(Colour)+1]
    except IndexError:
        Colour=Colours[0]
    Brush.color(Colour)

def Draw(x,y):
    Brush.pd()
def DontDraw(x,y):
    Brush.pu()

Brush.onclick(Draw)
Brush.onrelease(DontDraw)
Screen.onscreenclick(Blink,2)
Screen.onkeypress(Brush.clear,"c")
Screen.onkeypress(DecreaseSize,"1")
Screen.onkeypress(IncreaseSize,"2")
Screen.onkeypress(SwitchColour,"z")

def end():
    Screen.bye()
    exit()

for i in "q","e":
    Screen.onkeypress(Screen.bye,i)

def main():
    Screen.listen()
    while True:
        Brush.goto(PixelToCartesian(*Canvas.winfo_pointerxy()))
        Screen.update()
        

if __name__=="__main__":
    main()

print()
