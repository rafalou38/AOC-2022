#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct
{
    int start;
    int end;
} Elf;

int main()
{
    FILE *input = fopen("./04/input.txt", "r");
    if (input == NULL)
    {
        printf("Could not open input");
        exit(1);
    }

    unsigned char line[200];
    int sum = 0;
    while (!feof(input))
    {
        fgets(line, 200, input);

        Elf a, b;

        sscanf(line, "%d-%d,%d-%d", &a.start, &a.end, &b.start, &b.end);
        // printf("%d - %d , %d - %d \n", a.start, a.end, b.start, b.end);
        if (a.start < b.start && a.end < b.start)
        {
        }
        else if (a.start > b.end && a.end > b.end)
        {
        }
        else
        {
            sum++;
        }
        // if (a.start >= b.start && b.end >= a.end)
        // {
        //     sum++;
        //     // printf("yes\n");
        // }
        // else if (b.start >= a.start && b.end <= a.end)
        // {
        //     sum++;
        //     // printf("yes2\n");
        // }
    }

    fclose(input);
    printf("=> %d\n", sum);
    return 0;
}
