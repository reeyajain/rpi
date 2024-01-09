#include<stdio.h>
#include<stdlib.h>
#include<string.h>

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

int main() {
	printf("CPU temperature is %.2f°C",tempCelcius());
}
