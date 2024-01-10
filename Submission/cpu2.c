#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    float cpu_usage;

    fp = popen("mpstat 1 1 | grep '^%idle' | awk '{print $2}'", "r");
    if (fp == NULL) {
        perror("popen error");
        return 1;
    }

    if (fscanf(fp, "%f", &cpu_usage) != 1) {
        perror("fscanf error");
        return 1;
    }

    printf("CPU usage: %.2f%%\n", cpu_usage);

    pclose(fp);

    return 0;
}
