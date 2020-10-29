"""
Author: Gabriel Hofer
Instructor: Dr. Karlsson
Course: CENG-325 Program #2
Date: 11/16/2020
"""

class Assembler: 
  def __init__(self):
    self.instr2opcode = {
        "FMULS" : ['R', "00011110001"], 
        "FDIVS" : ['R', "00011110001"], 
        "FCMPS" : ['R', "00011110001"],
        "FADDS" : ['R', "00011110001"],
        "FSUBS" : ['R', "00011110001"]
        }
    self.shamt = {
        "FMULS" : "000010",
        "FDIVS" : "000110",
        "FCMPS" : "001000", 
        "FADDS" : "001010",
        "FSUBS" : "001110",
        }

  def asm2obj(line):
    
    

if __name__ == "__main__":
  assembler = Assembler()
  while(True):
    print(assembler.asm2obj(input()))



