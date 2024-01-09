#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){

FILE* file = fopen("/sys/class/thermal/thermal_zone0/temp","r");
if(file==NULL){

perror("Error opening file");
return 1;
}
int temperature;
fscanf(file,"%d",&temperature);
fclose(file);
float tempCelsius=temperature/1000.0;
printf("CPU Temperature:%.1fC\n",tempCelsius);
return 0;


}
