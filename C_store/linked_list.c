#include <stdio.h>
#include <stdlib.h>
/**
 * This code defines a node structure with two fields:
 * data and next. The add_node function adds a new node
 * to the beginning of the linked list. The delete_node function
 * deletes a node with the given data from the linked list.
 * The find_node function returns a pointer to the node with the
 * given data, or NULL if no such node exists. The main function
 * demonstrates how to use these functions to create,
 * modify, and search a linked list.
 */
struct node {
    int data;
    struct node* next;
};

struct node* head = NULL;

void add_node(int data) {
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = head;
    head = new_node;
}

void delete_node(int data) {
    struct node* temp = head;
    struct node* prev = NULL;
    while (temp != NULL && temp->data != data) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Node not found\n");
        return;
    }
    if (prev == NULL) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }
    free(temp);
}

struct node* find_node(int data) {
    struct node* temp = head;
    while (temp != NULL && temp->data != data) {
        temp = temp->next;
    }
    return temp;
}

int main() {
    add_node(1);
    add_node(2);
    add_node(3);
    add_node(4);
    add_node(5);

    printf("Initial linked list: ");
    struct node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");

    delete_node(3);

    printf("Linked list after deleting node with data 3: ");
    temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");

    struct node* node_2 = find_node(2);
    if (node_2 != NULL) {
        printf("Node with data 2 found\n");
    } else {
        printf("Node with data 2 not found\n");
    }

    return 0;
}
