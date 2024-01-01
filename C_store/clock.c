#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <colorama.h>
#include <pyfiglet.h>

/**
void time_set_sec(int count_sec)
{
	while (count_sec)
	{
		printf("count: %d to go\n", count_sec);
		sleep(1);
		count_sec--;
	}
	printf("We made it in 2024 !\n");
}
void print_newyear(char *love_future)
{
	char *looks = NULL;

	looks = (char *)malloc(strlen(love_future) * 10);
	strcpy(looks, love_future);
	printf("\033[1;34m%s\n]", looks);
	free(looks);
}

int main()
{
	int seconds;
	char *love_future = " Exception X ";

	printf("How many minute remaining to get into new year: ");
	scanf("%d", &seconds);
	time_set_sec(seconds);
	print_newyear(love_future);
	printf("Welcome to 2024 @Exception X.Clt!");
	return (0);
}*/


void time_set_sec(int count_sec)
{
	while (count_sec)
	{
		printf("count: %d to go\n", count_sec);
		sleep(1);
		count_sec--;
	}
	printf("We made it in 2024 !\n");
}

void print_newyear(char *love_future)
{
	char *looks = NULL;

	looks = (char *)malloc(strlen(love_future) * 10);
	strcpy(looks, love_future);
	printf(FG_BLUE "%s\n", looks);
	free(looks);
}

int main()
{
	int seconds;
	char *love_future = " Welcome to 2024 @innocent:) ";

	printf("Enter the countdown time in seconds: ");
	scanf("%d", &seconds);
	time_set_sec(seconds);
	print_newyear(love_future);
	return (0);
}
