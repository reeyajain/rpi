//this is final file
#include<stdio.h>
#include<string.h>
#include<time.h>
#include<unistd.h>

char *timeInstance() {
	time_t currentTime = time(NULL);
	char *time_str = ctime(&currentTime);
	time_str[strlen(time_str)-1] = '\0';
	return time_str;
}

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
	fclose(file);
	float cpuUsage = ((totalCpuTime - idleCpuTime)*100.0)/totalCpuTime;
	return cpuUsage;
}

float tempCelcius() {
	FILE *file = fopen("/sys/class/thermal/thermal_zone0/temp","r");
	if(file == NULL) {
		perror("Error opening temperature file");
		return 1;
	}
	int temperature;
	fscanf(file,"%d",&temperature);
	fclose(file);
	float tempCelcius = temperature/1000.0;
	return tempCelcius;
}

float mem() {
	FILE *file = fopen("/proc/meminfo","r");
	if(file == NULL) {
		perror("Error opening memory file");
		return 1;
	}
	char line[256];
	int totalMemory=0;
	int freeMemory=0;
	int availableMemory=0;
	while(fgets(line, sizeof(line), file)) {
		if(strstr(line,"MemTotal:")!=NULL) {
			sscanf(line, "%*s%d", &totalMemory);
		}
		else if(strstr(line,"MemFree:")!=NULL) {
			sscanf(line, "%*s%d", &freeMemory);
		}
		else if(strstr(line,"MemAvailable:")!=NULL) {
			sscanf(line, "%*s%d", &availableMemory);
		}
	}
	float mem_usage = 100.0*((float)totalMemory-(float)freeMemory)/totalMemory;
	return mem_usage;
}

int main() {
	FILE *file;
	file = fopen("data.txt","w+");
	if(ftell(file)==0)
		fprintf(file,"Time\tCPU\tMemory\tTemperature\n");
	for(int i=0; i<10000;i++) {
		fprintf(file,"%s\t%f\t%f\t%f\n",timeInstance(),cpu(),mem(),tempCelcius());
		fflush(file);
		sleep(2);
	}
}
