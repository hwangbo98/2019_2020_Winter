#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int num;
    
    long sum;
    char buffer[80];
    int n= 0;
    int l = 0;
    long fixed_costs = 0;
    long variable_costs = 0;
    long each_costs = 0;

    scanf("%ld %ld %ld", &fixed_costs, &variable_costs, &each_costs);

    while(1){
        if ( variable_costs > each_costs){
            printf("%d",-1);
            break;
        }
        else if ((fixed_costs+(variable_costs*n))<(each_costs*n)){
            printf("%d",n);
            break;
        }
        else {
            n++;
        }
    }
    
    
    return 0;
}