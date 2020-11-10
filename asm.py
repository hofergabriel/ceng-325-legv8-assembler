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
    self.i2o = json.load(open(filename))

  def imm2str(): pass

  """ list of tokens --> binary """
  def R(self,line): 
    return self.i2o[line[0]][1] + ' ' + \
        str(bin(int(line[3][1:]))[2:]).zfill(5) + ' ' + \
        self.i2o[line[0]][2] + ' ' + \
        str(bin(int(line[2][1:]))[2:]).zfill(5) + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(5)

  def I(self,line): 
    return self.i2o[line[0]][1] + ' ' + \
        str(bin(int(line[3][1:]))[2:]).zfill(12) + ' ' + \
        str(bin(int(line[2][1:]))[2:]).zfill(5) + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(5) + ' ' 

  def D(self,line): 
    return self.i2o[line[0]][1] + ' ' + \
        str(bin(int(line[3][1:]))[2:]).zfill(9) + ' ' + \
        "--" + \
        str(bin(int(line[2][1:]))[2:]).zfill(5) + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(5) + ' ' 

  def B(self,line): 
    return self.i2o[line[0]][1] + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(26)

  def CB(self,line): 
    return self.i2o[line[0]][1] + ' ' + \
        "--" + ' ' + \
        str(bin(int(line[1][1:]))[2:]).zfill(19) + ' ' + \
        str(bin(int(line[2][1:]))[2:]).zfill(5)

  def IW(self,line): 
    print("255: "+ str(int(line[2])))
    return self.i2o[line[0]][1] + ' ' + \
        str(int(line[2]))).zfill(16) + ' ' \
        str(bin(int(line[1][1:]))[2:]).zfill(5) + ' ' 

  """ whole instruction string --> binary
      determines which type of instruction """
  def asm2obj(self, line):
    line=list(filter(lambda i : i!='', re.split(",| |\[|\]|\n", line)))

    print(line)

    fmt = self.i2o[line[0]][0]
    if fmt == 'R':    return self.R(line)
    elif fmt == 'I':  return self.I(line)
    elif fmt == 'D':  return self.D(line)
    elif fmt == 'B':  return self.B(line)
    elif fmt == 'CB': return self.CB(line)
    else:             return self.IW(line)

""" Entry point """
def main():
  assembler = Assembler(sys.argv[1])
  while(True):
    s=input()
    if s=="quit": break
    print(assembler.asm2obj(s))

""" call main """
main()





