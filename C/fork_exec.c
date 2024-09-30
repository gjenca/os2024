#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

	pid_t pid; // int
	int status;

	if ((pid=fork())>0) {
		// Parent
		printf("Parent process; PID of child is %d\n",pid);
		wait(&status);
		printf("status:%d\n",WEXITSTATUS(status));
	}
	else {
		// Child
		printf("Child process; fork returned %d\n",pid);
		if (execl("/bin/ls","ls","/varr",NULL)) {
			perror("execl");
			exit(1);
		}

	}
	printf("Kapybara.\n");              

}

