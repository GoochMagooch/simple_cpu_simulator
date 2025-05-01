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
            reg_output = realloc(reg_output, (i + 1) * sizeof(char*));
            reg_output[i] = "Program ended";
            return 0;
        }
    }
    return 0;
}

int main() {
    char* test_arr[] = {"LOAD x", "test complete", "test", "END"};
    run_cpu(test_arr);
    return 0;
}