#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    FILE *input = fopen("./05/input.txt", "r");
    if (input == NULL)
    {
        printf("Could not open input");
        exit(1);
    }

    unsigned char line[200];
    while (!feof(input))
    {
        fgets(line, 200, input);
    }

    fclose(input);
    return 0;
}
