#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char **argv)
{
	FILE *file;
	size_t bufsize = 0;
	char *buff = NULL;
	char *tocken = NULL;
	int cov_int, count = 0;
	int p = 2, q;
	ssize_t gline;

	if (argc < 2)
	{
		printf("Error");
		exit(EXIT_FAILURE);
	}
	file = fopen(argv[1], "r");

	if (file == NULL)
	{
		return (0);
	}
	while (getline(&buff, &bufsize, file) != EOF)
	{
		tocken = strtok(buff, " \n");
		while (tocken != NULL)
		{
			tocken = strtok(NULL, " \n");
			count++;
		}
		cov_int = atoi(&tocken[count]);

		while (p < cov_int)
		{
			if (cov_int % p == 0)
			{
				q = cov_int / p;
				printf("%d=%d*%d\n", cov_int, q, p);
				break;
			}
			p++;
		}
	}
	return (0);
}
