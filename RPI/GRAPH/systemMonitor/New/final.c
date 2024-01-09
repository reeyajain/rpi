#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
/*
char* timeInstance(){

time_t currentTime;
struct tm*localTime;
currentTime = time(NULL);
localTime=localtime(&currentTime);
char* t = asctime(localTime);
printf("CurrentTime:%s",asctime(localTime));
return t;


}
long timeInstance(){

	time_t currentTime = time(NULL);
	return currentTime;

}
*/
float cpu(){

FILE* file = fopen("/proc/stat","r");
if(file==NULL){
perror("Error opening file");
return 1;
}
char line[256];
fgets(line,sizeof(line),file);
char cpu[5];
unsigned long user,nice,system,idle,iowait,irq,softirq;
sscanf(line,"%s %lu %lu %lu %lu %lu %lu %lu,",cpu,&user,&nice,&system,&idle,&iowait,&irq,&softirq);
unsigned long totalCpuTime = user + nice + system + idle + iowait + irq +softirq;
unsigned long idleCpuTime = idle;
fclose(file);
float cpuUsage =((totalCpuTime-idleCpuTime)*100.0)/totalCpuTime;
//printf("CPU Usage. %.2f% %\n",cpuUsage);
return cpuUsage;
}
float mem(){

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
}
fclose(file);

//printf("Total Memory:%d KB\n",totalMemory);
//printf("Free Memory:%d KB\n",freeMemory);
//printf("Available Memory:%d KB\n",availableMemory);
float memUsage = (float)availableMemory/totalMemory;
return	memUsage;
}

float temp(){

FILE* file = fopen("/sys/class/thermal/thermal_zone0/temp","r");
if(file==NULL){

perror("Error opening file");
return 1;
}
int temperature;
fscanf(file,"%d",&temperature);
fclose(file);
float tempCelsius=temperature/1000.0;
//printf("CPU Temperature:%.1fC\n",tempCelsius);
return tempCelsius;


}

void main(){
FILE* fptr = fopen("data.txt","w");

for(int i=1;i<2;i++)
{


	//if(fptr==NULL){
	fprintf(fptr,"Time\tCPU_Usag\tMemory_Usage\tCPU_Temperature\n");
	//}
	//else{
	int timeInstance=0;
	for(int i=0; i<10; i++)
	fprintf(fptr,"%d\t%f\t%f\t%f\n",++timeInstance,cpu(),mem(),temp());
	sleep(500);
}
	//mem();
	//temp();
	//timeInstance();
	//for(int j=1;j<1000;j++){
	//int x=0;
	//}
	//	}
}


