#include <stdarg.h>
#include <stdio.h>

void print_args(int count, ...) {
    va_list args;
    va_start(args, count);

    for (int i = 0; i < count; ++i) {
        printf("%d ", va_arg(args, int));
    }

    va_end(args);
}

int main() {
    int num_args;
    printf("Enter the number of arguments: ");
    scanf("%d", &num_args);

    int args[num_args];
    printf("Enter %d integers: ", num_args);
    for (int i = 0; i < num_args; ++i) {
        scanf("%d", &args[i]);
    }

    if (num_args >= 1) {
        print_args(num_args, args[0]);
    }
    if (num_args >= 2) {
        print_args(num_args, args[0], args[1]);
    }
    if (num_args >= 3) {
        print_args(num_args, args[0], args[1], args[2]);
    }

    return 0;
}
