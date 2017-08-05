GLD = 1.61803398875
sz = 800

def setup():
    size(sz, sz)
    noLoop()

def draw():
    background(255)
    resetMatrix()
    translate(width / 2, height)
    stroke(120, 88, 55)
    fill(20, 188, 18)
    tree(100)
    translate(width/3,0)
    tree(80)
    translate(-2*width/3,0)
    tree(110)
    
def leaf(w):
    ht = 4 * w
    wd = 4 * ht

    noStroke()
    rotate(PI / 4)
    ellipse(0, 0, wd, ht)
    rotate(HALF_PI)
    ellipse(0, 0, wd, ht)
    rotate(5 * PI / 4)  # 2PI - PI/4 - PI/2 = 5/4
    stroke(120, 88, 55)

def tree(w):
    w *= 1.0
    # rate which width is shrinking
    # probability of branch at a certain width
    # degree of evenness in the branch
    # the above determines the angles they come out at (bigger branch, less
    # rotation)

    minw = 1

    def branch(lw):
        p = (1 - lw / w) ** 2 * 300 + 100
        r = random(1000)
        return p > r

    def chase(ln):
        line(0, 0, 0, ln)
        translate(0, ln)

    def limb(lw):
        while lw > minw:
            strokeWeight(lw)
            chase( (1 - lw / w) - 5)
            z = 1.2
            if branch(lw):
                ba = random(z)  # left
                bb = z - ba  # right

                pushMatrix()
                rotate(-HALF_PI/4 * bb / z)
                limb(lw * ba)
                popMatrix()

                rotate(HALF_PI/4 * ba / z)
                lw *= bb/z
            else: 
                lw -= lw/w + .1
        leaf(lw)

    pushMatrix()
    limb(w)
    popMatrix()
