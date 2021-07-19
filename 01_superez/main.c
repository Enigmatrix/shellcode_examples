#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/mman.h>

int setup() {
    // turn off buffering, then printing to stdout etc will be better
    setbuf(stdin,   NULL);
    setbuf(stdout,  NULL);
    setbuf(stderr,  NULL);
}

// fools to trust user input, really
int is_valid(void* buffer) {
    return 1;
}

int main() {
    setup();

    void* buffer = mmap((void*)0x1337000, 0x1000, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (buffer < 0) {
        perror("cannot allocate buffer");
        exit(-1);
    }
    read(0, buffer, 0x1000);

    if (is_valid(buffer)) {
        ((void (*)(void)) buffer) ();
    }
}