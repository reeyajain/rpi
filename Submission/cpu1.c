#include<sys/resource.h>
#include<stdio.h>

int main() {
    double loadavg[3];

    if (getloadavg(loadavg, 3) != 0) {
        perror("getloadavg error");
        return 1;
    }

    printf("CPU load for 1 minute: %.2f%%\n", loadavg[0] * 100);
    printf("CPU load for 5 minutes: %.2f%%\n", loadavg[1] * 100);
    printf("CPU load for 15 minutes: %.2f%%\n", loadavg[2] * 100);

    return 0;
}
