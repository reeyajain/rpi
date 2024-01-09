#include<stdio.h>
#include<time.h>

char *timeInstance() {
	time_t currentTime;
	struct tm *localTime;
	currentTime = time(NULL);
	localTime = localtime(&currentTime);
	char *a = asctime(localTime);
	return a;
}

int main() {
	printf("Current time: %s",timeInstance());
}
