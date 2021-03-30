#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
    int flag, qt;
    char line[3000], first, next, *token;
    while (fgets(line, 3000, stdin) != NULL) {
        flag = 1;
        first = toupper(line[0]);
        if (first == '*')
            exit(0);
        qt = 0;
        // dividir a linha pelo \n
        token = strtok(line, " \n");
        while (token != NULL) {
            next = toupper(token[0]);
            // a cada divisao de " ", token recebe a proxima palavra
            token = strtok(NULL, " ");
            // se as proximas letras forem != da da primeira
            // nao temos um tautograma
            if (first != next)
                flag = 0;
            qt++;
        }
        if (flag || !qt)
            printf("Y\n");
        else
            printf("N\n");
    }
    return 0;
}
