ssave = None
sz = 800
def setup():
    global ssave
    
    size(sz, sz)
    ssave = createGraphics(sz, sz)
    noLoop()


def draw():
    ssave.beginDraw()
    ssave.background(255)
    resetMatrix()
    ssave.translate(width * 5 / 9, height - 20)
    tree(70, 30, 5, TAU/5,PI/8)
    ssave.endDraw()
    ssave.save("tree5.tif")
    image(ssave, 0, 0)

def the(n, m, ln):
    #
    m -= (sin(n)) ** 2 * (m / TAU) if ln > 10 else (1/cos(m)) ** 2 * \
        (n / PI)  # sqrt(13)
    return(m)

def leaf(ln, st):
    ssave.noStroke()
    ssave.fill(20, 188, 18)
    ssave.ellipse(0, 15, 22, 5)

    ssave.ellipse(0, 8, 25, 6)
    ssave.ellipse(0, 0, 15, 4)

def branch(ln, st, t):
    ssave.stroke(120, 88, 55)
    ssave.strokeWeight(st)
    pushMatrix()
    ssave.line(0, 0, 0, -ln)  # if ln > 13 else leaf(ln, st)
    ssave.translate(0, -ln)  # if st <  else ssave.translate(0, -ln *st/6 )
    popMatrix()

def left(ln, sln, st, n, m, t):
    ssave.rotate(sin(t / 13))
    branch(ln, st, t)
    ssave.rotate(sin(-t))
    ssave.pushMatrix()
    ssave.rotate(sin(t))
    branch(ln, st, t)
    ssave.popMatrix()

def right(ln, sln, st, n, m, t):
    ssave.rotate(sin(t))
    branch(ln, st, t)
    ssave.rotate(sin(-t / 4))
    ssave.pushMatrix()
    ssave.rotate(sin(t / 8))
    branch(ln, st, t)
    ssave.popMatrix()


def leftr(ln, sln, st, n, m, t):
    ssave.rotate(sin(t / 4))
    branch(ln, st, t)
    ssave.rotate(sin(-t / 7))
    ssave.pushMatrix()
    ssave.rotate(sin(t / 13))
    branch(ln, st, t)
    ssave.rotate(sin(-t / 8))
    ssave.popMatrix()
   
    right(ln, sln, st, n, m, t)

def rightr(ln, sln, st, n, m, t):
    ssave.rotate(sin(-t / 3))
    branch(ln, st, t)
    ssave.rotate(sin(-t / 37))
    ssave.pushMatrix()
    # ssave.rotate(t)
    tree(ln, sln, st, n, m)
    ssave.rotate(sin(t / 4))
    branch(2 * ln, st, t)
    ssave.popMatrix()
    left(ln, sln, st, n, m, t)
    #branch(ln, st, t)


def tree(ln, sln, st, n, m):
    it = ln / sln
    t = the(n, m, ln)

    branch(ln, st, t)

    ssave.rotate(sin(-t / 4))

    ssave.rotate(sin(t / 2))

    #branch(ln, st, t)
    #global i
    if it > ln - 1:
        leaf(ln, st)

    if ln > sln:
        pass
        left(ln, sln, st, n, m, t)
        right(ln, sln, st, n, m, t)
        # ssave.rotate(cos(-t/50))
        branch(ln, st, t)
        ln *= (.61803)
        st *= .69 if st > .8 else 1
        #tree(ln, sln, st, n, m)
        right(ln, sln, st, n, m, t)
        leftr(ln, sln, st, n, m, t)
        right(ln, sln, st, n, m, t)
        #tree(ln, sln, st, n, m)
        #right(ln, sln, st, n, m, t)
        tree(ln, sln, st, n, m)
        
