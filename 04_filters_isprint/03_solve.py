from pwn import *
context.arch = 'amd64'

p = process("./filters_isprint")

# pls find real shellcode
shellcode = b""
print(shellcode)

p.send(shellcode)
p.interactive()