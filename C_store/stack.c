#include <stdio.h>
#include <stdlib.h>

#define SIZE 4

int top = -1;
int inp_array[SIZE];

void push()
{
    int x;

    if (top == SIZE - 1)
    {
        printf("\nOverflow!! The stack is full.");
    }
    else
    {
        printf("\nEnter the element to add to the stack: ");
        scanf("%d", &x);
        top += 1;
        inp_array[top] = x;
    }
}

void pop()
{
    if (top == -1)
    {
        printf("\nUnderflow!! The stack is empty.");
    }
    else
    {
        printf("\nPopped element: %d", inp_array[top]);
        top -= 1;
    }
}

void show()
{
	int i;
    if (top == -1)
    {
        printf("\nUnderflow!! The stack is empty.");
    }
    else
    {
        printf("\nElements present in the magical stack: \n");
        for (i = top; i >= 0; --i)
            printf("%d\n", inp_array[i]);
    }
}

int main()
{
    int choice;

    while (1)
    {
        printf("\nenter actio of your coice on the stack:");
        printf("\n1. Add an element (Push)\n2. Remove an element (Pop)\n3. Peek at the top (Top)\n4. Exit");
        printf("\n\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                show();
                break;
            case 4:
                exit(0);
            default:
                printf("\nInvalid choice! Try another action.");
        }
    }
}
