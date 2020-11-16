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
Assembler
self.FLAGS: flags register
"""
class Assembler: 

  """ open json file """
  def __init__(self,f1,f2):
    self.FLAGS = {}
    self.i2o = json.load(open(f1))
    self.b_cond = json.load(open(f2))

  """ immediate value --> binary string """
  def imm2bits(self,word): 
    if word[0]=='#' : return str(bin(int(word[1:]))[2:])
    return str(bin(int(word,16))[2:])

  """ maps branch-conditional instructions to their code """
  def B_cond(self,word):
    if word[0]=='B' : return self.b_cond[word]
    else: return '-'

  """ list of tokens --> binary """
  def R(self,line): 
    return self.i2o[line[0]][1] + \
        bin(int(line[3][1:]))[2:].zfill(5) + \
        self.i2o[line[0]][2] + \
        bin(int(line[2][1:]))[2:].zfill(5) + \
        bin(int(line[1][1:]))[2:].zfill(5)

  def I(self,line): 
    return self.i2o[line[0]][1] + \
        bin(int(line[3][1:]))[2:].zfill(12) + \
        bin(int(line[2][1:]))[2:].zfill(5) +  \
        bin(int(line[1][1:]))[2:].zfill(5)   

  def D(self,line): 
    return self.i2o[line[0]][1] + \
        bin(int(line[3][1:]))[2:].zfill(9) + \
        "00" + \
        bin(int(line[2][1:]))[2:].zfill(5) + \
        bin(int(line[1][1:]))[2:].zfill(5) 

  def B(self,line): 
    return self.i2o[line[0]][1] + \
        self.imm2bits(line[1]).zfill(26)

  def CB(self,line): 
    return self.i2o[line[0]][1] + \
        self.imm2bits(line[2]).zfill(19) + \
        bin(int(line[1][1:]))[2:].zfill(5)

  def IW(self,line): 
    return self.i2o[line[0]][1] + \
        bin(int(line[4])//16)[2:].zfill(2) + \
        self.imm2bits(line[2]).zfill(16) + \
        bin(int(line[1][1:]))[2:].zfill(5) 

  def B_COND(self,line):
    return self.i2o["B.cond"][1] + \
        self.imm2bits(line[1]).zfill(19) + \
        self.b_cond[line[0]]

  """ whole instruction string --> binary
      determines which type of instruction """
  def asm2obj(self, line):
    line=list(filter(lambda i : i!='', re.split(",| |\[|\]|\n", line)))
    print(line)
    if(line[0][0:2]=='B.'): 
      return self.B_COND(line)
    fmt = self.i2o[line[0]][0]
    if fmt == 'R':    return self.R(line)
    elif fmt == 'I':  return self.I(line)
    elif fmt == 'D':  return self.D(line)
    elif fmt == 'B':  return self.B(line)
    elif fmt == 'CB': return self.CB(line)
    else:             return self.IW(line)

""" puts spaces in the string every four bits """
def nibbles(s):
  ret=""
  for i in range(len(s)):
    ret+=s[i]
    if (i+1)%4==0: ret+=' '
  return ret

""" Entry point """
def main():
  assembler = Assembler(sys.argv[1],sys.argv[2])
  while(True):
    s=input()
    if s=="quit": break
    print(nibbles(assembler.asm2obj(s)))

""" call main """
main()





