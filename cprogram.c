#include <stdio.h>
#include <stdlib.h>

void call_python_script() 
{
    int ret = system("pythonscript.py");
    if (ret == -1) {
        perror("Error calling Python script");
        exit(1);
    }
}
void file_printer(char filename[]) 
{
    FILE *fp;
    fp=fopen(filename,"r");
    if(fp==NULL)
    {
        perror("Error while opening fiile");
        exit(0);
    }
    char ch;
    while((ch=fgetc(fp))!=EOF) putchar(ch);
    fclose(fp);
}



int main() {
    FILE *file;
    char string[100];

    printf("Enter the name of the recipe you want :");
    scanf("%s",string);

    file = fopen("prompt.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "%s\n", string);
    fclose(file);
    printf("String written to the file successfully.\n");
    call_python_script();
    file_printer("result.txt");
    return 0;
}
