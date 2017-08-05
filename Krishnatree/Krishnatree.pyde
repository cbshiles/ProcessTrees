sz = 800
def setup():
    size(sz, sz)
    noLoop()
    
    global dir
    dir = os.path.join(os.getcwd(),"images")

def draw():
    background(255)
    resetMatrix()
    
    translate(width * 3 / 9, height - 20)
    
    #tree(len, stop len, width of tree, two thetas)
    tree(100, 30, 5, 2,1)
    
def fnk():
    i= 1.0/1000
    try:
        lzt = next(os.walk(dir))[2]
    except :
        return "000"

    lzt.sort()
    num = lzt[-1][0:-4] # number of file, filename w/o .tif
    t=str(float(num )/1000+ i)[2:]
    return t
    
def keyPressed():
    if key == 's':
        x = os.path.join(dir, fnk())
        print("Saved at "+x)
        save(x)

def tree(ln, sln, st, n, m):

    def leaf():
        noStroke()
        fill(20, 188, 18)
        ellipse(0, 15, 22, 5)
        
        ellipse(0, 8, 25, 6)
        ellipse(0, 0, 15, 4)
            
    def branch():
        stroke(120, 88, 55)
        strokeWeight(st)
        line(0, 0, 0, -ln)  # if ln > 13 else leaf(ln, st)
        translate(0, -ln)  # if st <  else translate(0, -ln *st/6 )
        
    def left():
        rotate(sin(t / 13))
        branch()
        rotate(sin(-t))
        pushMatrix()
        rotate(sin(t))
        branch()
        popMatrix()
        
    def right():
        rotate(sin(t))
        branch()
        rotate(sin(-t / 4))
        pushMatrix()
        rotate(sin(t / 8))
        branch()
        popMatrix()
        
            
    def leftr():
        rotate(sin(t / 4))
        branch()
        rotate(sin(-t / 7))
        pushMatrix()
        rotate(sin(t / 13))
        branch()
        rotate(sin(-t / 8))
        popMatrix()
        
        right()
            
    def rightr():
        rotate(sin(-t / 3))
        branch()
        rotate(sin(-t / 37))
        pushMatrix()
        # rotate(t)
        rotate(sin(t / 4))
        branch()
        popMatrix()
        left()
        #branch(ln)

    def the():
        z = 40#(sin(n)) ** 2 * (m / TAU) if ln > 10 else (1/cos(m)) ** 2 * \
             #(n / PI)  # sqrt(13)
        return m-z
    
    def run():
        tree(ln, sln, st, n, m)

    it = ln / sln 
    t = the()


    branch()
            
    rotate(sin(-t / 4))
    
    rotate(sin(t / 2))
    
    #branch(ln, st, t)
    #global i
    if it > ln - 100:
        leaf()
        
        if ln > sln:
        
            
            ln *= (.61803)
            st *= .69 if st > .8 else 1
            rotate(PI/13)
            left()
            rotate(-PI/2)
            rotate(-PI/3)
            rightr()
            rotate(PI/3)
            rotate(sin(PI/5))
            left()
            rotate(sin(PI/3))
            run() 
    