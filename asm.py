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
  def R(self,line): 
    ret = self.i2o[line[0]][1] + ' ' + \
        str(bin(int(line[3][1:]))[2:]).zfill(5) + ' ' + \
        self.i2o[line[0]][2] + ' ' + \
        str(bin(int(line[2][1:]))[2:]).zfill(5) + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(5)
    return ret

  def I(self,line): 
    ret = self.i2o[line[0]][1] + ' ' + \
        str(bin(int(line[3][1:]))[2:]).zfill(12) + ' ' + \
        str(bin(int(line[2][1:]))[2:]).zfill(12) + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(12) + ' ' 
    return ret

  def D(self,line): pass
  def B(self,line): pass
  def CB(self,line): pass
  def IW(self,line): pass


  """ whole instruction string --> binary
      determines which type of instruction """
  def asm2obj(self, line):
    line=list(filter(lambda i : i!='', re.split(",| |\n", line)))
    print(line)
    fmt = self.i2o[line[0]][0]
    if fmt == 'R': ret=self.R(line)
    elif fmt == 'I': ret=self.I(line)
    elif fmt == 'D': ret=self.D(line)
    elif fmt == 'B': ret=self.B(line)
    elif fmt == 'CB': ret=self.CB(line)
    else: ret=self.IW(line)
    return ret

""" Entry point """
def main():
  print("sys.argv: "+str(sys.argv))
  assembler = Assembler(sys.argv[1])
  print("this is the Assembler!")
  while(True):
    print(assembler.asm2obj(input()))

""" call main """
main()





