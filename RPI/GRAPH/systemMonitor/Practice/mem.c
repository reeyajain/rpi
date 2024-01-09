#include<stdio.h>
#include<stdlib.h>
#include<string.h>

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
//	printf("%d %d %d",totalMemory, freeMemory, availableMemory);
	float mem_usage = 100.0*((float)totalMemory-(float)availableMemory)/totalMemory;
	return mem_usage;
}

int main() {
	printf("Percentage of memory usage is %.2f%\n",mem());
}
