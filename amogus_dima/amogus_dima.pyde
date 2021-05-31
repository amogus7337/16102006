x=0
y=0
s=0
def setup ():
    global img1,img2,img3,img4,img5
    size (800,800)
    img1 = loadImage(u'птица2.png')
    img2 = loadImage(u'птица1.png')
    img3 = loadImage(u'мишень.png')
    img4 = loadImage(u'мишень 1.png')
    img5 = loadImage(u'мишень 2.png')
    imageMode(CENTER)
#управление птицай
def draw ():
    global x,y,s
    background (211,128,128)
    circle(mouseX,mouseY,50)
    image(img1,mouseX,mouseY)
    image(img3,725,550)
    image(img4,725,250)
    image(img5,725,400)
    rect(x,y,100,30)
    text (x,20,20)
    textSize(20)
    s=+1
    x+=620
    if mousePressed:
       x = mouseX
       y = mouseY
 
