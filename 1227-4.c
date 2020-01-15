#include <stdio.h>
#include <stdlib.h>

int main(){
    float gs_25[2];
    float N_store = 0;
    float min = 0;
    float *other_store, *total_price;
    int count = 0;
    scanf("%f %f", &gs_25[0], &gs_25[1]);

    scanf("%f", &N_store);

    other_store = (float*) malloc(sizeof(float)*(N_store*2));
    total_price = (float*) malloc(sizeof(float)*(N_store));
    for(int i = 0 ; i<N_store*2; i+=2){
        scanf("%f %f", &other_store[i], &other_store[i+1]);
        fflush(stdin);
    }

    float gs_25_price= (gs_25[0]/gs_25[1]) * 1000;
    /* 
    for(int i = 0; i<N_store*2; i++){
        printf("%.2f ", other_store[i]);
    }
    printf("\n"); */
    for (int k = 0; k<N_store; k++){
        for (int j = 2*k; j<(2*k)+1; j++){
            total_price[k] = (other_store[j]/other_store[j+1]) * 1000;
            //printf("%.2f\n",total_price[k]);
        }
        count++;
    }
    min = gs_25_price ;
    
    for(int i = 0; i<N_store; i++){
        if(min > total_price[i]){
            min = total_price[i];
        }
    }
    printf("%.2f",min);
     
    //printf("%.2f",gs_25_price);

    




}