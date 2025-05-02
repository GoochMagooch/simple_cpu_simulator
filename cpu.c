#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// int number = 69;
// char buffer[20];
// sprintf(buffer, "%d", number); converts int to string
// printf("String version: %d: ", buffer)

char** run_cpu(char** instructions, int arr_length) {
    char** reg_output = NULL;
    int regis = 0;

    for (int i = 0; i < arr_length; i++) {
        reg_output = realloc(reg_output, (i + 1) * sizeof(char*));

        if (!strcmp(instructions[i], "END")) {
            reg_output[i] = "Program ended";
            return reg_output;
        }

        reg_output = realloc(reg_output, (i + 1) * sizeof(char*));
        reg_output[i] = instructions[i];
    }

    return reg_output;
}

int main() {
    char* instruction_set[] = {"LOAD x", "test complete", "test", "END"};
    int length = sizeof(instruction_set) / sizeof(instruction_set[0]);
    char** output = run_cpu(instruction_set, length);

    for (int i = 0; i < length; i++) {
        if (i == length - 1) {
            printf("%s\n", output[i]);
        } else {
            printf("%s, ", output[i]);
        }
    }

    free(output);
    return 0;
}