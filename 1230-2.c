#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    unsigned int num;
    
    int sum;
    char buffer[80];
    int n= 0;
    int l = 0;
    int o_count = 0;
    int x_count = 0;


    scanf("%d", &num);
    char *arr[num];
    int count[num];
    while(n<num){
        sum =0;
        o_count = 0;
        scanf("%s", buffer);

        l = strlen(buffer);

        for(int i=0; i<l; i++){
            if(buffer[i] == 'O'){
                
                o_count++;
                sum+=o_count;
                
                
            }
            else if(buffer[i] == 'X'){
                o_count = 0;
                sum+=o_count;
            }
        }
        count[n] = sum ;

    }
    for(int i=0; i<num; i++){
        printf("%d\n",count[i]);
    }
    return 0;
}

