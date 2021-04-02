# Caroline Ninganga
# Project09 
# Version 3 
# 03/29/2021

import turtle_interpreter as ti
import shapes
import tree

def scene():

    s = shapes.Square()
    s.setColor( (0.3, 0.5, 0.3) )
    s.draw(-400, -1000, scale=8, orientation=90)

    s = shapes.Square()
    s.setColor( (0.3, 0.5, 0.3) )
    s.draw(0, -100, scale=0.8, orientation=90)


    s = shapes.Square()
    s.setColor( (0.5, 0.6, 0.6) )
    s.draw(-100, -100, scale=2, orientation=90)

    t = shapes.Triangle()
    t.setColor( (0.5, 0.4, 0.4) )
    t.draw(100, 100, scale=2, orientation=180)


    #create the first shape hexagon
    h = shapes.circle()
    h.setColor( (0.4, 0.4, 0.2) )
    h.draw( -300, 350, scale=0.5, orientation=12 )

    # #create the first shape hexagon
    # h = shapes.circle()
    # h.setColor( (0.6, 0.5, 0.1) )
    # h.draw( 0, 300, scale=0.5, orientation=12 )

    # tr = tree.Tree( distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None )
    tr = tree.Tree( filename='systemH.txt') # asign tr to the tree object 
    tr.setColor( (0.5, 0.3, 0.4) )
    tr.draw(-300, -200, scale=2, orientation=90)

    # tr = tree.Tree( distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None )
    tr = tree.Tree( filename='systemH.txt') # asign tr to the tree object 
    tr.setColor( (0.5, 0.3, 0.4) )
    tr.draw(300, -200, scale=2, orientation=90)

    # # tr = tree.Tree( distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None )
    # tr = tree.Tree( filename='systemJ.txt') # asign tr to the tree object 
    # tr.setColor( (0.5, 0.3, 0.4) )
    # tr.draw(100, -75, scale=2, orientation=90)

    # # tr = tree.Tree( distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None )
    # tr = tree.Tree( filename='systemH.txt') # asign tr to the tree object 
    # tr.setColor( (0.5, 0.3, 0.4) )
    # tr.draw(-80, -75, scale=2, orientation=90)
  

      # wait
    ti.TurtleInterpreter().hold()

if __name__ == '__main__':
    scene()
