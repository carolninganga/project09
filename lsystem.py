# Caroline Ninganga
# Project09 
# Version 3 
# 03/29/2021

import sys
import random 

class Lsystem: 

    # wirte a constructor 
    def __init__( self, filename=None):
         # assign to the field base, the empty string
         self.base = " "
         # assign to the field rules, the empty dictionary
         self.rules = {}
         # if the filename variable is not equal to None
         if filename != None:
            # call the read method of self with filename as the argument
            self.read( filename )

    # get the base value of the base field of the object
    def getBase(self):
        return self.base

    #get rule should return the specified rule of self
    def getRule(self, index):
        return self.rules[index]
    #the setBase function should assign to the base field (self.base) the value in b.
    def setBase(self, b):
        self.base = b
    #the addRule function should append newrule to the rules field of self
    def addRule(self, newrule):
        # mydict['F'] = ['FF', 'F+F-F']
        # mydict represents the dictionary object
        # 'F' represents the key
        # ['FF', 'F+F-F'] represents the value
        # rule = [symbol, replacement1, replacment2, ...]
        self.rules[newrule[0]] = newrule[1:] # Key = 0 and Value = [replacement1, replacement2,...]

    # numsRules retruns the number of rules in the rules list 
    def numRules(self):
        return len(self.rules)

    # write a read method
    def read( self, filename ):
        # assign to the rules field of self the empty list
        self.rules = {}
        # assign to a variable (e.g. fp) the file object created with filename in read mode
        fp = open(filename)
        # for each line in fp 
        for line in fp:
            # assign to line the result of calling line.strip()
            line = line.strip()
            # assign to a variable (e.g. words) the result of calling the split() method line
            words = line.split()
            # if the first item in words is equal to the string 'base'
            #print("Words: ", words)
            #words = ['base', base]
            #words = ['rule',[symbol, replacement]]
            if words[0] == 'base':
                # call the setBase method of self with the new base string
                self.setBase(words[1])
            # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
                # call the addRule method of self with the new rule (the slice of words from index 1
                self.addRule(words[1:])

        # call the close method of the file
        fp.close()


    def replace(self, istring):
        # assign to a local variable (e.g. tstring) the empty string
        tstring = ""
        # for each character c the original string (istring)
        for c in istring:
            # if the character c is in the self.rules dictionary
            if c in self.rules:
                # add to tstring a random choice from the dictionary entry self.rules[c]
                tstring = tstring + random.choice(self.rules[c])
            # else
            else:
                # add to tstring the character c
                tstring = tstring + c
        # return tstring
        return tstring

    def buildString(self, iterations):
        # assign to a local variable (e.g. nstring) the base field of self
        nstring = self.base
        # for the number of iterations
        for i in range(iterations):
            # assign to nstring the result of calling the replace method of self with nstring as the argument
            nstring = self.replace( nstring)
        # return nstring
        return nstring

def main(argv):

    # check the number of arguments entered by the user 
    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

if __name__ == "__main__":
    main(sys.argv)
