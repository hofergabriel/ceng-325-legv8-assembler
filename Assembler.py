"""
Author: Gabriel Hofer
Instructor: Dr. Karlsson
Course: CENG-325 Program #2
Date: 11/16/2020
"""
import re


"""
Assembler

self.FLAGS: flags register

"""
class Assembler: 
  def __init__(self):
    self.FLAGS = {}
    self.instr2opcode = {
        "FMULS" : ['R', '00011110001', '000010'], 
        "FDIVS" : ['R', '00011110001', '000110'], 
        "FCMPS" : ['R', '00011110001', '001000'],
        "FADDS" : ['R', '00011110001', '001010'],
        "FSUBS" : ['R', '00011110001', '001110']

        "FMULD" : ['R', '00011110011', '000010'],
        "FDIVD" : ['R', '00011110011', '000110'],
        "FCMPD" : ['R', '00011110011', '001000'],
        "FADDD" : ['R', '00011110011', '001010'],
        "FSUBD" : ['R', '00011110011', '001110'],

        "STURB" : []
        "LDURB" : []
        "B.cond" : []
        "STURH" : []
        "LDURH" : []
        "AND" : []
        "ADD" : []
        "ADDI" : []
        "ANDI" : []
        "BL" : []

        "SDIV" : ['R', '10011010110', '000010' ],
        "UDIV" : ['R', '10011010110', '000011' ],
        "MUL"  : ['R', '10011011000', '011111' ],

        "SMULH" : []
        "UMULH" : []
        "ORR" : []
        "ADDS" : []
        "ADDIS" : []
        "ORRI" : []

        "CBS" : []
        "CBNZ" : []
        "STURW" : []
        "LDURSW" : []
        "STURS" : []
        "LDURS" : []
        "STXR" : []
        "EOR" : []
        "SUB" : []
        "SUBI" : []
        
        "EORI" : []
        "MOVZ" : []
        "LSR" : []
        "LSL" : []
        "BR" : []
        "ANDS" : []
        "SUBS" : []
        "SUBIS" : []
        "ANDIS" : []
        "MOVK" : []
        "STUR" : []
        "LDUR" : []
        "STURD" : []
        "LDURD" : []
        








        }

  def asm2obj(self, line):
    line=re.split(",| ", line)

    print(self.instr2opcode[line[0]][1])

    return str(line)


"""
Entry point
"""
def main():
  assembler = Assembler()
  while(True):
    print(assembler.asm2obj(input()))

""" 
call main
"""
main()






















