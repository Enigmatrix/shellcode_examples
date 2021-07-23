from pwn import *
from capstone import *
import sys

# charset = [b"\x00" ... b"\x0f"]
charset = [x.to_bytes(1, 'little') for x in range(16)]

md = Cs(CS_ARCH_X86, CS_MODE_64)
prev = b""

def info(op):
    instrs = list(md.disasm(op, 0))

    if len(instrs) == 1:
        instr = instrs[0]
        g = instr.mnemonic+" "+instr.op_str

        global prev
        if g != prev:
            print("%s :\t%s" %(repr(op), g)) # print instruction if it's not a repeat
            prev = g

# recursively bruteforce all combinations
def level(op, n):
    if n == 0:
        info(op)
    else:
        for c in charset:
            level(op+c, n-1)

level(b'', int(args.LEVEL))

# python3 gen.py LEVEL=5