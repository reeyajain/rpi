#include<stdio.h>
#include<stdlib.h>
#include<string.h>

float cpu() {
	FILE *file = fopen("/proc/stat","r");
	if(file == NULL) {
		perror("error opening cpu file");
		return 1;
	}
	char line[256];
	fgets(line,sizeof(line),file);
	char cpu[5];
	unsigned long user, nice, system, idle, iowait, irq, softirq;
	sscanf(line, "%s %lu %lu %lu %lu %lu %lu %lu", cpu,&user,&nice,&system,&idle,&iowait,&irq,&softirq);
	unsigned long totalCpuTime = user + nice + system + idle + iowait + irq + softirq;
	unsigned long idleCpuTime = idle;
	printf("%lu\n",totalCpuTime);
	printf("%lu\n",idleCpuTime);
	printf("%lu\n",totalCpuTime-idleCpuTime);
	fclose(file);
	float cpuUsage = ((idleCpuTime)*100.0)/totalCpuTime;
	return cpuUsage;
}

int main() {
	printf("CPU Usage: %.5f%\n",cpu());
}
