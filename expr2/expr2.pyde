GLD = .61803398875
sz = 800
def setup():
    size(sz,sz)
    noLoop()
    
def draw():
    background(255)
    resetMatrix()
    translate(width/2, height)
    x = .2
    scale(x,x)
    stroke(120, 88, 55)
    fill(20, 188, 18)
    tree(120)

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

def tree(wd):
    def limb(w, mode, z):
        if w < 1:
            leaf(w)
            return

        chase(-w*6,w)
    
        wa = .8
        wb = GLD
        #tdg = PI/4.0+(wd-w)*PI/(2*wd)
        tdg = PI/12.0 + PI/3.0*(wd-w)/wd
        wr = wb/wa
        rot1 = -tdg/(1+wr)
        rot0 = tdg + rot1  
    
        oldmode = mode
        
        mode = 2*(z==1 and mode==1)-1
        
        z = oldmode
    
        pushMatrix()  
        rotate(rot0*mode)
        limb(w*wa,-1,z)
        popMatrix()
        
        rotate(rot1*mode)
        limb(w*wb,1,z)
        
    limb(wd,1,1)