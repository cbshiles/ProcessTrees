sz = 1000
def setup():
    global ssave
    
    size(sz, sz)
    ssave = createGraphics(sz, sz)

    # ssave.size(1000,1000)
    noLoop()
    # ssave.strokeJoin(ROUND)


def draw():
    ssave.beginDraw()
    ssave.background(255)
    #ssave.translate(width/2, height)

    ssave.translate(width * 4 / 9, height - 190)
    tree(ssave, 160, 5, PI, 4.7)
    ssave.resetMatrix()
    #ssave.translate(width / 2, height * 5 / 6)
    tree(ssave, 160 * 4 / 9,  5, PI,  4.7 )
    ssave.endDraw()
    ssave.save("tree5.tif")
    image(ssave, 0, 0)
    #
# test(200,7)
def the(n, m):
    m = PI/(cos(m) + sin(n))
    return(m)


def branch(ssave, len, st):
    ssave.noFill()
    ssave.strokeWeight(st)
    ssave.ellipseMode(CORNERS)
    # ssave.ellipse(0,0,len/st,len)
    ssave.line(0, 0, 0, -len) #if len > 3.8029 else ssave.ellipse(0, 0, len, len / 2 * st)
    # ssave.arc(-len,-len,len,len,0,the)
    ssave.translate(0, -len)   if st < 498  else ssave.translate(0,-len/st)

def tree(ssave, len, st, n, m):
    t = the(m, n)
    n = n
    m = m
    branch(ssave, len, st)
    if len > 5:
        #the += 1.618
        len *= (.66)
        st *= .69 if st > .8 else 1

        ssave.pushMatrix()
        ssave.rotate(-t)
        tree(ssave, len, st, n, m)
        ssave.popMatrix()

        branch(ssave, len, st)

        ssave.pushMatrix()
        ssave.rotate(t)
        tree(ssave, len, st, n, m)
        ssave.popMatrix()
        
        ssave.rotate(-t)
        branch(ssave, len, st)
        tree(ssave, len, st, n, m)

    else:
        pass
        #
