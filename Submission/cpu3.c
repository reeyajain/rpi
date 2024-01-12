#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    FILE *fp;
    unsigned long long user1, nice1, system1, idle1, iowait1, irq1, softirq1, steal1, guest1, guest_nice1;
    unsigned long long user2, nice2, system2, idle2, iowait2, irq2, softirq2, steal2, guest2, guest_nice2;
    unsigned long long total1, total2;
    float cpu_usage;

    while (1) {
        // Read the first set of CPU statistics
        fp = fopen("/proc/stat", "r");
        if (fp == NULL) {
            printf("Error opening /proc/stat\n");
            exit(1);
        }
        fscanf(fp, "cpu  %llu %llu %llu %llu %llu %llu %llu %llu %llu %llu",
               &user1, &nice1, &system1, &idle1, &iowait1, &irq1, &softirq1, &steal1, &guest1, &guest_nice1);
        fclose(fp);

        // Wait for a second
        sleep(1);

        // Read the second set of CPU statistics
        fp = fopen("/proc/stat", "r");
        if (fp == NULL) {
            printf("Error opening /proc/stat\n");
            exit(1);
        }
        fscanf(fp, "cpu  %llu %llu %llu %llu %llu %llu %llu %llu %llu %llu",
               &user2, &nice2, &system2, &idle2, &iowait2, &irq2, &softirq2, &steal2, &guest2, &guest_nice2);
        fclose(fp);

        // Calculate the total CPU time
        total1 = user1 + nice1 + system1 + idle1 + iowait1 + irq1 + softirq1 + steal1 + guest1 + guest_nice1;
        total2 = user2 + nice2 + system2 + idle2 + iowait2 + irq2 + softirq2 + steal2 + guest2 + guest_nice2;

        // Calculate the CPU usage percentage
        cpu_usage = 100.0 * ((total2 - total1) - (idle2 - idle1)) / (total2 - total1);

        // Print the CPU usage
        printf("CPU usage: %.2f%%\n", cpu_usage);
    }

    return 0;
}
