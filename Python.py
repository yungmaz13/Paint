from turtle import Screen as _Screen, Turtle

Colours=["black","grey","white","red","yellow","pink","green","orange","violet","purple","blue","aqua","lime"]

Screen=_Screen()
Screen.setup(1.0,1.0)
Screen.title("Paint")
Screen.tracer(0,0)

Canvas=Screen.getcanvas()
Width,Height=Canvas.winfo_width(),Canvas.winfo_height()
HalfWidth,HalfHeight=Width//2,Height//2

Brush=Turtle("circle")
Brush.color(Colours[0])
Brush.speed(0)
Brush.penup()
Brush.pensize(16)

Background=Turtle()
Background.ht()
Background.speed(0)

def BackgroundColour(Colour:str="white"):
    Background.clear()
    Background.penup()
    Background.goto(-HalfWidth,-HalfHeight)
    
    Background.color(Colour)
    Background.begin_fill()
    
    Background.goto(HalfWidth,-HalfHeight)
    Background.goto(HalfWidth,HalfHeight)
    Background.goto(-HalfWidth,HalfHeight)
    Background.goto(-HalfWidth,-HalfHeight)
    
    Background.end_fill()

    Background.penup()
    Background.home()

xp,xc=range(Width+1),range(-HalfWidth,HalfWidth+1)
yp,yc=range(Height+1),range(-HalfHeight,HalfHeight+1)
def PixelToCartesian(x:float,y:float):
    Offset=5 # Relative to monitor
    try:
        return xc[xp.index(x)]-Offset,-yc[yp.index(y)]+Offset*10
    except ValueError:
        return xc[xp.index(x)]-Offset,-yc[-1]+Offset*5

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
    try:
        Brush.color(Colours[Colours.index(Brush.color()[0])+1])
    except IndexError:
        Brush.color(Colours[0])

def SwitchBackgroundColour():
    try:
        BackgroundColour(Colours[Colours.index(Background.color()[0])+1])
    except IndexError:
        BackgroundColour(Colours[0])

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
Screen.onkeypress(SwitchBackgroundColour,"x")

def end():
    Screen.bye()
    exit()

for i in "q","e":
    Screen.onkeypress(end,i)

def Post():
    Brush.ht()
    Directory="desktop/Paint.eps"
    Canvas.postscript(file=Directory)
    Brush.st()
    
    return

Screen.onkeypress(Post,"Return")

def main():
    Screen.listen()
    while True:
        Brush.goto(PixelToCartesian(*Canvas.winfo_pointerxy()))
        Screen.update()
        

if __name__=="__main__":
    main()

print()
