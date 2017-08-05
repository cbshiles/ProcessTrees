GLD = .61803398875
sz = 800

def setup():
    size(sz,sz)
    noLoop()
    
def draw():
    background(255)
    resetMatrix()
    translate(width/2, height*7/6)
    x = .20
    scale(x,x)
    stroke(120, 88, 55)
    fill(20, 188, 18)
    tree(160,1,3)

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
    
def chase(ln,w):
    strokeWeight(w)
    line(0, 0, 0, ln)
    translate(0, ln)
            
def tree(w,mode,z):
    if w < 1:
        leaf(w)
        return
    
    if z == 3:
        mode *= -1
    elif z == 1:
        mode *= -1
    elif z == 0:
        z = 4
    
    z -= 1
    
    pushMatrix()
    chase(-w*6,w)
    deg = PI/12.0

    rotate(deg*mode)
    tree(w*.8,mode,z)
    rotate(deg*3*-mode)
    tree(w*GLD,mode,z)
    popMatrix()