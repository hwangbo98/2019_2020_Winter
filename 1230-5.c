#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int num = 0;
    int *height;
    int *width;
    int **arr;
    int sum = 0;
    //int *count;
    int cell_num = 0;
    scanf("%d", &num);
    
    height = (int*)malloc(sizeof(int)*num);
    width = (int*) malloc(sizeof(int)*(num));
    arr = (int**)malloc(sizeof(int*)*(*height));
    for(int i=0; i<*height; i++){
        arr[i] = (int*)malloc(sizeof(int*)*(*width));
    }


    //count = (int*)malloc(sizeof(int)*num);
    for(int k =0; k<num; k++){
        scanf("%d", &height[k]);
        scanf("%d", &width[k]);
        
    }
    printf("%d",*height);

    for(int k =0; k<num; k++){
        for(int i=0; i<height[k]; i++){
            for(int j=0; j<width[k]; j++){
                if(i==0 && j==0){
                    arr[i][j] = 1;
                }
                else{
                    if(i==0){
                        sum += j+1;
                        arr[i][j] = sum;
                        printf("%d\n",arr[i][j]);
                    }
                }
            }
        }
    }
    
    return 0;
}