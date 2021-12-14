#include <stdio.h>

int main(int argc, char * argv[])
{
 char theString[400];

 strcpy(theString, argv[1]);

 printf("You entered: %s\n", theString);
 return 0;
}
