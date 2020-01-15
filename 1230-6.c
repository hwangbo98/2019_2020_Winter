#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int n_value = 0;
    int m_value = 0;
    int *str;
    char input[200];
    char *s;
    char *p;
    int cnt = 0;
    int sum = 0;
    scanf("%d %d", &n_value, &m_value);

    str = (int*)malloc(sizeof(int)*n_value);
    //s = (char*)malloc(sizeof(char)*(n_value*2));
    scanf("%s", input);
    strcpy(s,input);
    p = strtok(input," ");
    while(p!=NULL){
        str[cnt] = atoi(p);
        cnt++;
        p = strtok(NULL," ");
    }

    for(int i=0; i<cnt; i++){
        sum+=str[i];
        printf("%d\n",str[i]);
    }
    printf("%d",sum);
    return 0;
}
