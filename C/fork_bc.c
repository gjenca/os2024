#include <stdio.h>
#include <unistd.h>

int main() {

	pid_t pid; // int
	int pipeA[2];
	int pipeB[2];
	static char buf[100];
	static char zadanie[100];
	FILE *vyraz;
	FILE *vysledok;
	int i;
	
	pipe(pipeA);
	pipe(pipeB);

	if ((pid=fork())>0) {
		// Parent
		printf("Parent process; PID of child is %d\n",pid);
		vyraz=fdopen(pipeA[1],"w");
		vysledok=fdopen(pipeB[0],"r");
		close(pipeB[1]);
		close(pipeA[0]);
		for (i=0;i<10;i++) {
			sprintf(zadanie,"%d*7\n",i);
			fprintf(vyraz,zadanie);
			fflush(vyraz);
			fscanf(vysledok,"%s",buf);
			printf("%s\n",buf);
		}
	}
	else {
		// Child
		printf("Child process; fork returned %d\n",pid);
		dup2(pipeB[1],1);
		dup2(pipeA[0],0);
		close(pipeB[0]);
		close(pipeA[1]);
		close(pipeB[1]);
		close(pipeA[0]);
		execl("/bin/bc","bc",NULL);

	}
	printf("Kapybara.\n");              

}

