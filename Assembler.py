"""
Author: Gabriel Hofer
Instructor: Dr. Karlsson
Course: CENG-325 Program #2
Date: 11/16/2020
"""
import re
import json
import sys

"""
check this shit out:
https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/
"""

"""
Assembler
self.FLAGS: flags register
"""
class Assembler: 

  """ open json file """
  def __init__(self,filename):
    self.FLAGS = {}
    print("filename: "+filename)
    f=open(filename)
    self.i2o = json.load(f)

  """ list of tokens --> binary """
  def R(self,line): pass
  def I(self,line): pass
  def D(self,line): pass
  def B(self,line): pass
  def CB(self,line): pass
  def IW(self,line): pass

  """ whole instruction string --> binary
      determines which type of instruction """
  def asm2obj(self, line):
    line=re.split(",| ", line)
    fmt = self.i2o[line[0]][0]
    if fmt == 'R': self.R(line)
    elif fmt == 'I': self.I(line)
    elif fmt == 'D': self.D(line)
    elif fmt == 'B': self.B(line)
    elif fmt == 'CB': self.CB(line)
    else: self.IW(line)

    print(self.i2o[line[0]][1])
    return str(line)


""" Entry point """
def main():
  print("sys.argv: "+str(sys.argv))
  assembler = Assembler(sys.argv[1])
  print("this is the Assembler!")
  while(True):
    print(assembler.asm2obj(input()))

""" call main """
main()





