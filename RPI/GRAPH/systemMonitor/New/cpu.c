#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
int f(){

FILE* file = fopen("/proc/stat","r");
if(file==NULL){
perror("Error opening file");
return 1;
}
char line[256];
fgets(line,sizeof(line),file);
//printf("%s",line); print first line of  stat file
char cpu[5];
unsigned long user,nice,system,idle,iowait,irq,softirq;
sscanf(line,"%s %lu %lu %lu %lu %lu %lu %lu,",cpu,&user,&nice,&system,&idle,&iowait,&irq,&softirq);
unsigned long totalCpuTime = user + nice + system + idle + iowait + irq +softirq;
unsigned long idleCpuTime = idle;
fclose(file);
float cpuUsage =((totalCpuTime-idleCpuTime)*100.0)/totalCpuTime;
printf("CPU Usage. %.2f% %\n",cpuUsage);
return 0;
}

void main(){

for(int i=1;i<100;i++)
{
	f();
}
}
