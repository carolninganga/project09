# Caroline Ninganga
# Test file for question 2 
# Python project 9

import turtle_interpreter
import shapes

def main():

    #create the first shape hexagon
    h = shapes.Hexagon()
    h.setColor( (0.6, 0.8, 0.9) )
    h.draw( -200, 200, scale=0.6, orientation=12 )

    #create the first shape hexagon
    h = shapes.Star()
    h.setColor( (0.3, 0.9, 0.9) )
    h.draw( 0, 200, scale=0.6, orientation=12 )

     #create the first shape hexagon
    h = shapes.circle()
    h.setColor( (0.3, 0.2, 0.2) )
    h.draw( 200, 200, scale=0.6, orientation=12 )

      # wait
    turtle_interpreter.TurtleInterpreter().hold()


if __name__ == '__main__':
    main()
