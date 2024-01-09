#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){

FILE* file = fopen("/proc/meminfo","r");
if(file==NULL){
perror("Error opening file");
return 1;
}
char line[256];
int totalMemory =0,freeMemory=0,availableMemory=0;
while(fgets(line,sizeof(line),file)){
	if(strstr(line,"MemTotal:")!=NULL){
		sscanf(line,"%*s %d",&totalMemory);
	}
	else if(strstr(line,"MemFree:")!=NULL){

		sscanf(line,"%*s %d",&freeMemory);
	}
	else if(strstr(line,"MemAvailable:")!=NULL){
		sscanf(line,"%*s %d",&availableMemory);
	}
//	printf("%s",line);
}
fclose(file);

printf("Total Memory:%d KB\n",totalMemory);
printf("Total Memory:%d KB\n",freeMemory);
printf("Available Memory:%d KB\n",availableMemory);
return 0;



}
