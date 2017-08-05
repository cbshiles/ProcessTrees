GLD = .61803398875
sz = 800
def setup():
    
    size(sz,sz)
    noLoop()
    
def draw():
    background(255)
    resetMatrix()
    translate(width/2, height)
    x = .17
    scale(x,x)
    stroke(120, 88, 55)
    fill(20, 188, 18)
    tree(160,-1,1)

def leaf(w):
    ht = 4*w
    wd = 4*ht
    
    noStroke()
    rotate(PI/4)
    ellipse(0, 0, wd, ht)    
    rotate(HALF_PI)
    ellipse(0, 0, wd, ht)    
    rotate(5*QUARTER_PI)#2PI - PI/4 - PI/2 = 5/4
    stroke(120, 88, 55)
    
def chase(ln,w):
    strokeWeight(w)
    line(0, 0, 0, ln)
    translate(0, ln)
            
def tree(w,mode,z):
    if w < 1:
        leaf(w)
        return
    
    mode *=  z
    
    pushMatrix()
    chase(-w*6,w)
    deg = PI/13.0

    rotate(deg*mode)
    tree(w*.8,mode,-z)
    rotate(deg*3*-mode)
    tree(w*GLD,-mode,-z)
        
    popMatrix()