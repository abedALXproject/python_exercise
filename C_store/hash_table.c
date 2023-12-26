#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct hash_node_s
{
    char *key;
    char *value;
    struct hash_node_s *next;
} hash_node_t;

typedef struct hash_table_s
{
    unsigned long int size;
    hash_node_t **array;
} hash_table_t;

hash_table_t *create_hash_table(unsigned long int size)
{
    hash_table_t *new_table = malloc(sizeof(hash_table_t));
    new_table->size = size;
    new_table->array = calloc(size, sizeof(hash_node_t *));
    return new_table;
}

unsigned long int hash_function(char *key, unsigned long int size)
{
    unsigned long int hash_value = 0;
    for (int i = 0; i < strlen(key); i++)
    {
        hash_value += key[i];
    }
    return hash_value % size;
}

void insert(hash_table_t *table, char *key, char *value)
{
    unsigned long int index = hash_function(key, table->size);
    hash_node_t *new_node = malloc(sizeof(hash_node_t));
    new_node->key = key;
    new_node->value = value;
    new_node->next = table->array[index];
    table->array[index] = new_node;
}

char *lookup(hash_table_t *table, char *key)
{
    unsigned long int index = hash_function(key, table->size);
    hash_node_t *current_node = table->array[index];
    while (current_node != NULL)
    {
        if (strcmp(current_node->key, key) == 0)
        {
            return current_node->value;
        }
        current_node = current_node->next;
    }
    return NULL;
}

int main()
{
    hash_table_t *table = create_hash_table(10);
    insert(table, "John", "555-1234");
    insert(table, "Jane", "555-5678");
    char *john_number = lookup(table, "John");
    printf("John's phone number is %s\n", john_number);
    char *jane_number = lookup(table, "Jane");
    printf("Jane's phone number is %s\n", jane_number);
    return 0;
}
