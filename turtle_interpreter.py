# Caroline Ninganga
# Project09 
# Version 3 
# 03/29/2021

#import the turtle package, the random and sys packages
import turtle as t
import sys
import random

#define a TurtleInterpreter
class TurtleInterpreter:
    initialized = False
    #define the init
    def __init__(self, dx = 800, dy = 800):
        #This helps the __init__ method to not create another turtle window if it already exists.
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
        # call turtle.setup with dx and dy as the arguments
        t.setup( dx, dy )
        # set the turtle tracer to false (optional)
        t.tracer( False )

    def drawString(self, string, distance, angle ):
        """ Interpret the characters in string as a series of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the angle (in degrees) for each right 
        or left command. The list of turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position 
        """

        # assign to stack the empty list
        stack = []
        #define a color stack
        colorstack = []
        # for each character d in string 
        for c in string :
            # if d is equal to 'F'
            if c == 'F' :
                # tell the turtle go forward by distance
                t.forward( distance )
            # else if c is equal to '-'
            elif c == '-':
                t.right( angle )
            # else if d is equal to '+'
            elif c == '+':
                t.left( angle )
            # else if d is equal '['
            elif c == '[':
                # append to stack the position of the turtle (position method)
                stack.append(t.position())
                # append to stack the heading of the turtle (heading method)
                stack.append(t.heading())
            # else if c is  equal to ']'
            elif c == ']':
                # tell the turtle to pick up pen 
                t.up()
                # call the setheading method of the turtle and pass it the value popped off stack
                t.setheading( stack.pop())
                # call the goto method of the turtle and pass it the value popped of stack
                t.goto(stack.pop())
                # tell the turtlr to put down pen
                t.down()

            #'<' - the left angle bracket should push the current turtle color onto a color stack
            #this function returns a tuple of colors (two sub-lists of rgb values)
            elif c == '<':
                colorstack.append( t.color()[0] )
            
            #'>' - the right angle bracket should pop the current turtle color off the color stack and set the 
            # turtle's color to that value using the turtle.color function.
            elif c == '>':
                t.color(colorstack.pop())
            elif c == 'g':
                t.color(0.15, 0.5, 0.2)
            elif c == 'y':
                t.color(0.8, 0.8, 0.3)
            elif c == 'r':
                t.color(0.7, 0.2, 0.3)
            elif c == '{':
                t.begin_fill()
            elif c == '}':
                t.end_fill()

            #Add two cases to drawString. For the character '{' call turtle.begin_fill(), and for the character '}' call turtle.end_fill()            

        # call the turtle.update() (not in the for loop)
        t.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        t.hideturtle()
        t.update()

        # Close the window when users presses the 'q' key
        t.onkey(t.bye, 'q')

        # Listen for the q button press event
        t.listen()

        # Have the turtle listen for a click
        t.exitonclick()


    #def place(self, xpos, ypos, angle=None): - the method should pick up the pen, place the turtle at location (xpos, ypos), 
    # orient the turtle if the angle argument is not None, and then put down the pen.
    def place(self, xpos, ypos, angle=None):
        t.up()
        t.goto( xpos, ypos )
        if angle != None:
            self.orient( angle )
        # tell the turtlr to put down pen
        t.down()

    #def orient(self, angle): - the method should use the turtle's setheading function to set turtle's heading to the given angle.
    def orient( self, angle ):
        t.setheading(angle)

    #def goto(self, xpos, ypos): - the method should pick up the turtle, send the turtle to (xpos, ypos), and then put the pen down.
    def goto( self, xpos, ypos ):
        t.up()
        t.goto( xpos, ypos )
        t.down()

    #def setColor(self, c): - the method should call turtle.color() with the argument c to set the turtle's color.
    def setColor( self, c ):
        t.color( c )

    #def setWidth(self, w): - the method should call turtle.width() with the argument w to set the turtle's width.
    def setWidth( self, w ):
        t.width( w )
