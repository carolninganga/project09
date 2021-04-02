# Caroline Ninganga
# Project09 
# Version 3 
# 03/29/2021


import turtle_interpreter
import shapes

#creates one tile 
def tile( x, y, scale ):
    s = shapes.Square()
    #s. setColor( (0.3, 0.4, 0.4 ) )
    s.draw(0, 100, scale=0.8, orientation=8)

    return s
 
 
def mosaic(x, y, scale, Nx, Ny ):
    tile(x, y, scale)



def main():

   
    tile(0, 100, 10)


    # wait
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main()



# def mosaic(x, y, scale, Nx, Ny )

    # ti = turtle_interpreter.TurtleInterpreter()

    # square = 'F-F-F-F-'
    