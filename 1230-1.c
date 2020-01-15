#include <stdio.h>
#include <stdlib.h>

int main(){
    unsigned int num;
    int *arr;
    int sum;
    scanf("%d", &num);
    arr = (int*) malloc(sizeof(int)*(num*3));
    for (int i=0; i<num; i++){
        scanf("%d %d",&arr[(2*i)+1], &arr[(2*i)+2]);
    }

    for(int j=0; j<num; j++){
        sum = arr[(2*j)+1] + arr[(2*j)+2];
        printf("%d\n",sum);
    }
    free(arr);
}