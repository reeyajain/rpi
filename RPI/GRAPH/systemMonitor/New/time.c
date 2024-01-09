#include<stdio.h>
#include<time.h>
#include<string.h>
int main(){

/*time_t currentTime;
struct tm*localTime;
currentTime = time(NULL);
localTime=localtime(&currentTime);
printf("CurrentTime:%s",asctime(localTime));
return 0;
*/
time_t mytime = time(NULL);
char* time_str = ctime(&mytime);
time_str[strlen(time_str)-1]='\0';
printf("Current Time : %s",time_str);
printf("HI,I am Time");
return 0;

}
