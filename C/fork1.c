#include <stdio.h>
#include <unistd.h>

int main() {

	pid_t pid; // int

	if ((pid=fork())>0) {
		// Parent
		printf("Parent process; PID of child is %d\n",pid);
	}
	else {
		// Child
		printf("Child process; fork returned %d\n",pid);

	}
	printf("Kapybara.\n");              

}

