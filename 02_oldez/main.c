#include <stdio.h>
#include <unistd.h>

int setup() {
    // turn off buffering, then printing to stdout etc will be better
    setbuf(stdin,   NULL);
    setbuf(stdout,  NULL);
    setbuf(stderr,  NULL);
}

int main() {
    setup();

    char name[0x40];

    printf("Enter your name at %p: ", name);    // OwO what's this
    read(0, name, 0x400);                       // uwu, too big?
}