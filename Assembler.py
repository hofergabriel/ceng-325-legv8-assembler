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
        'B'      : ['B', '000101'],

        'FMULS'  : ['R', '00011110001', '000010'], 
        'FDIVS'  : ['R', '00011110001', '000110'], 
        'FCMPS'  : ['R', '00011110001', '001000'],
        'FADDS'  : ['R', '00011110001', '001010'],
        'FSUBS'  : ['R', '00011110001', '001110']

        'FMULD'  : ['R', '00011110011', '000010'],
        'FDIVD'  : ['R', '00011110011', '000110'],
        'FCMPD'  : ['R', '00011110011', '001000'],
        'FADDD'  : ['R', '00011110011', '001010'],
        'FSUBD'  : ['R', '00011110011', '001110'],

        'STURB'  : ['D']
        'LDURB'  : ['D']
        'B.cond' : ['CB']
        'STURH'  : ['D']
        'LDURH'  : ['D']
        'AND'    : ['R', '10001010000' ]
        'ADD'    : ['R', '10001011000' ]
        'ADDI'   : ['I']
        'ANDI'   : ['I']
        'BL'     : ['B']

        'SDIV'   : ['R', '10011010110', '000010' ],
        'UDIV'   : ['R', '10011010110', '000011' ],
        'MUL'    : ['R', '10011011000', '011111' ],

        'SMULH'  : ['R', '10011011010']
        'UMULH'  : ['R', '10011011110']
        'ORR'    : ['R', '10101010000']
        'ADDS'   : ['R', '10101011000']

        'ADDIS'  : ['I']
        'ORRI'   : ['I']

        'CBZ'    : ['CB']
        'CBNZ'   : ['CB']
        'STURW'  : ['D']
        'LDURSW' : ['D']

        'STURS'  : ['R', '10111100000']
        'LDURS'  : ['R', '10111100010']

        'STXR'   : ['D']
        'LDXR'   : ['D']
        'EOR'    : ['R', '11001010000']

        'SUB'    : ['R', '11001011000']
        'SUBI'   : ['I']
        
        'EORI'   : ['I']
        'MOVZ'   : ['IM']
        'LSR'    : ['R', '11010011010']
        'LSL'    : ['R', '11010011011']
        'BR'     : ['R', '11010110000']
        'ANDS'   : ['R', '11101010000']
        'SUBS'   : ['R', '11101011000']
        'SUBIS'  : ['I']
        'ANDIS'  : ['I']
        'MOVK'   : ['IM']
        'STUR'   : ['D']
        'LDUR'   : ['D']
        'STURD'  : ['R', '11111100000']
        'LDURD'  : ['R', '11111100010']

        }

  """
    list of tokens --> binary 
  """
  def R(self,line): pass
  def I(self,line): pass
  def D(self,line): pass
  def B(self,line): pass
  def CB(self,line): pass
  def IW(self,line): pass

  """
    whole instruction string --> binary
    determines which type of instruction 
  """
  def asm2obj(self, line):
    line=re.split(",| ", line)
    fmt = self.instr2opcode[line[0]][0]
    if fmt == 'R': self.R(line)
    else if fmt == 'I': self.I(line)
    else if fmt == 'D': self.D(line)
    else if fmt == 'B': self.B(line)
    else if fmt == 'CB': self.CB(line)
    else self.IW(line)

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


















