# Always save this thing

def fnk():
    i= 1.0/1000
    try:
        lzt = next(os.walk(dir))[2]
    except :
        return "000"

    lzt.sort()
    print("lzt",lzt)
    word = lzt[-1][0:-4]
    t=str(float(word )/1000+ i)[2:]
    return t
    
def keyPressed():
    if key == 's':
        x = os.path.join(dir, fnk())
        print("path",x)
        save(x)

GLD = .61803398875
sz = 800
def setup():
    
    size(sz,sz)   
    noLoop() 
    
    global dir
    dir = os.path.join(os.getcwd(),"images")
    
def draw():
    background(255)
    resetMatrix()
    translate(width/2, height)
    stroke(120, 88, 55)
    fill(20, 188, 18)
    f = .55
    scale(f,f)
    tree(140)
    
def leaf(w):
    ht = 4*w
    wd = 4*ht
    
    noStroke()
    rotate(PI/4)
    ellipse(0, 0, wd, ht)    
    rotate(HALF_PI)
    ellipse(0, 0, wd, ht)    
    rotate(5*PI/4)#2PI - PI/4 - PI/2 = 5/4
    stroke(120, 88, 55)
            
def tree(w):
    if w < 1:
        leaf(w)
        return
    strokeWeight(w)
    pushMatrix()
    ln = -w*2.0
    line(0, 0, 0, ln)
    translate(0, ln)
    deg = PI/13.0
    w *= GLD+.1
    rotate(-deg)
    tree(w)
    rotate(2*deg)
    tree(w)
    popMatrix()