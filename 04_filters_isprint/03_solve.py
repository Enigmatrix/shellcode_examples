from pwn import *
context.arch = 'amd64'

p = process("./filters_isprint")

shellcode = b""
print(shellcode)

p.send(shellcode)
p.interactive()