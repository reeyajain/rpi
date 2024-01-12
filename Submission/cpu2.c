#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFF 256

double getCPUIdle() {
    FILE* pipe = popen("mpstat 1 1 | grep '^Average' | awk '{print $NF}'", "r");
    if (!pipe) {
        perror("Error opening pipe");
        return -1.0;
    }

    char buffer[MAX_BUFF];
    if (!fgets(buffer, sizeof(buffer), pipe)) {
        perror("Error reading pipe");
        pclose(pipe);
        return -1.0;
    }

    pclose(pipe);

    double idleTime = atof(buffer);
    double cpuTime = 100-idleTime;
    return cpuTime;
}

int main() {
while(1){
    double idle = getCPUIdle();
    if (idle < 0.0) {
        printf("Failed to retrieve CPU idle time.\n");
    } else {
        printf("CPU Time: %.2f%%\n", idle);
    }
}
    return 0;
}
