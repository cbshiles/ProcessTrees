def setup():
    size(1000,1000)
    noLoop()
    
def draw():
    tree(5,300)
    tree2(5,300)
    
def branch(n, len):
    line(0,0,0,-len)

def rotl(n,len):
    rotate(-PI/6)
    pushMatrix()
    branch(n,len)
    popMatrix()
    #rotr(n,len)
    rotate(PI/2)
    pushMatrix()
    translate(0,-len)
    
    branch(n,len)
    popMatrix()
    #rotr(n,len)
    
def rotr(n, len):
    branch(n,len)
    translate(0,-len)
    branch(n,len)
    rotate(PI/3)
    branch(n,len)
    rotate(-PI/6)
    #pushMatrix()
    branch(n,len)




def rotl2(n,len):
    rotate(PI/4)
    pushMatrix()
    branch(n,len)
    popMatrix()
    #rotr(n,len)
    rotate(-PI/7)
    pushMatrix()
    translate(0,-len)
    
    branch(n,len)
    popMatrix()
    #rotr(n,len)
    
def rotr2(n, len):
    branch(n,len)
    translate(0,-len)
    branch(n,len)
    rotate(-PI/7)
    branch(n,len)
    rotate(-PI/6)
    #pushMatrix()
    branch(n,len)


def tree(n, len):
    resetMatrix()
    translate(width/3, height)
    branch(n, len)
    translate(0,-len)
    while n > 0:
        
        rotl(n,len)
        rotr(n,len)
        #pushMatrix()
        #popMatrix()
        
        len *= .67
        n -= 1
        
    pass
        
def tree2(n, len):
    resetMatrix()
    translate(width/3, height)
    branch(n, len)
    translate(0,-len)
    while n > 0:
        
        rotl2(n,len)
        rotr2(n,len)
        #pushMatrix()
        #popMatrix()
        
        len *= .67
        n -= 1
        
    pass
