#include <stdlib.h>
#include <stdio.h>

// int number = 69;
// char buffer[20];
// sprintf(buffer, "%d", number); converts int to string
// printf("String version: %d: ", buffer)

char* run_cpu(char** instructions) {
    char* reg_output[100];
    int regis = 0;

    for (int i = 0; i < 100; i++) {
        if (instructions[i] == "END") {
            printf("Program ended\n");
            return 0;
        } else {
            printf("%s, ", instructions[i]);
        }
    }
    return 0;
}

int main() {
    char* test_arr[] = {"LOAD x", "test complete", "test", "END"};
    run_cpu(test_arr);
    return 0;
}