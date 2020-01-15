#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int num = 0;
    int *height;
    int *width;
    int *count;
    int cell_num = 0;
    scanf("%d", &num);
    height = (int*)malloc(sizeof(int)*num);
    width = (int*) malloc(sizeof(int)*(num));
    count = (int*)malloc(sizeof(int)*num);
    for(int k =0; k<num; k++){
        cell_num = 0;
        scanf("%d %d %d", &height[k], &width[k], &count[k]);
        
        
    }
    for(int k =0; k<num; k++){
        cell_num = 0;
        
        for(int i=1; i<width[k]+1; i++){
            for(int j=1; j<height[k]+1; j++){
                cell_num++;
                if(count[k] == cell_num){
                    printf("%d%02d\n",j,i);
                    break;
                }
            }
        }
    }
    return 0;
}