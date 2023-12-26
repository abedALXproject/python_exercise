#include <stdio.h>
#include <stdlib.h>

stack = []  # Imagine this as our stack of plates

# Pushing an element onto the stack
def push(element):
    stack.append(element)  # Add the plate (element) to the top

# Popping an element from the stack
def pop():
    if len(stack) == 0:
        return "Underflow"  # Oops, no plates left!
    else:
        return stack.pop()  # Remove the topmost plate

# Checking if the stack is empty
def isEmpty():
    return len(stack) == 0

# Example usage:
push("Magic Spell")  # Adding a plate with a spell
push("Dragon Roar")  # Adding another plate
print(pop())  # Removing the topmost plate (prints "Dragon Roar")
print(isEmpty())  # Is the stack empty? (prints False)
