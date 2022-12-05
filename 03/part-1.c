#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int getScore(char c)
{
    if (c > 64 && c < 91)
        return c - 38;
    else
        return c - 96;
}

int main()
{
    FILE *input = fopen("./03/input.txt", "r");
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
        int len = strlen(line) - 1;

        unsigned char count[128] = {0};
        unsigned char issue = 0;

        for (int i = 0; i < len; i++)
        {
            if (i >= len / 2 + 1)
            {
                if (count[line[i]] > 0)
                {
                    issue = line[i];
                    break;
                }
            }
            else
            {
                count[line[i]]++;
            }
        }
        int score = getScore(issue);
        sum += score;
        printf("%c : %d\n", issue, score);
    }

    fclose(input);
    printf("=> %d\n", sum);
    return 0;
}
