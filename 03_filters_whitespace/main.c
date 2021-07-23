#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/mman.h>

int setup() {
    // turn off buffering, then printing to stdout etc will be better
    setbuf(stdin,   NULL);
    setbuf(stdout,  NULL);
    setbuf(stderr,  NULL);
}

// fools to trust user input, really
int is_valid(void* buffer) {
    char* chars = (char*)buffer;
    for(int i = 0; i < 0x1000; i++) {
        if (isspace(chars[i])) {
            return 0;
        }
    }
    return 1;
}

void* create_rwx() {
    void* buffer = mmap(
        (void*)0x1337000,                       // allocate memory @ 0x1337000 ..
        0x1000,                                 // with size 0x1000 ..
        PROT_READ | PROT_WRITE | PROT_EXEC,     // with perms read-write-exec (rwx)
        MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    if (buffer < 0) {
        perror("cannot allocate buffer");
        exit(-1);
    }
    return buffer;
}

int main() {
    setup();

    void* buffer = create_rwx();
    read(0, buffer, 0x1000);

    if (is_valid(buffer)) {
        ((void (*)(void)) buffer) (); // 'call' the buffer
    }
}