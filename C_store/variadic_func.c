#include <stdio.h>
#include <stdarg.h>

void print_ints(int count, ...) {
    va_list args;
    va_start(args, count);

    for (int i = 0; i < count; i++) {
        int num = va_arg(args, int);
        printf("%d ", num);
    }

    va_end(args);
}

int main() {
    printf("Printing some numbers: ");
    print_ints(5, 10, 20, 30, 40, 50);
    printf("\n");

    return 0;
}
