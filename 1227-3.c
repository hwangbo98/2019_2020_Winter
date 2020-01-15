#include <stdio.h>
#include <stdlib.h>

int main(){
    int input[9];
    int sum = 0;
    for (int i =0; i<9; i++){
        scanf("%d", & input[i]);
        sum += input[i];
    }

    for (int j =0; j<8; j++){
        for(int k=j+1; k<9; k++){
            if(sum - (input[j] + input[k]) == 100){
                for(int z =0; z<9; z++){
                    if(z!=j && z!=k){
                        printf("%d\n",input[z]);
                    }
                }
            }
        }
    }
}